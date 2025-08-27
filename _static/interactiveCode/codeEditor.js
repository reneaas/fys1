


class CodeEditor {
    constructor(editorId) {
        this.editorId = editorId;          // ID of the HTML textarea element to convert to a code editor
        this.loadAddons().then(() => {
            this.editor = this.initializeEditor(editorId); // Initialize the CodeMirror editor instance
            this.editor = this.addCommentOverlay(this.editor); // Add custom overlay for highlighting comments
            this.setupThemeListener();         // Set up a listener to detect and apply theme changes
            this.refreshOnVisibilityChange(); // Add this line
        });

        // this.editor = this.initializeEditor(editorId); // Initialize the CodeMirror editor instance
        // this.editor = this.addCommentOverlay(this.editor); // Add custom overlay for highlighting comments
        // this.setupThemeListener();         // Set up a listener to detect and apply theme changes
        // this.refreshOnVisibilityChange(); // Add this line
    }

    /**
     * Initializes the CodeMirror editor with custom settings.
     * @param {string} editorId - The ID of the textarea element to enhance with CodeMirror.
     * @returns {Object} - The initialized CodeMirror editor instance.
     */
    initializeEditor(editorId) {
        return CodeMirror.fromTextArea(document.getElementById(editorId), {
            mode: {
                name: "python",            // Language mode set to Python
                version: 3,                 // Python 3 syntax
            },
            lineNumbers: true,             // Enable line numbers
            theme: this.getCurrentTheme(), // Set the initial theme based on user preference
            tabSize: 4,                    // Set the tab size for indentation
            indentUnit: 4,                 // Number of spaces per indentation level
            matchBrackets: true,          // Highlight matching brackets
            autoCloseBrackets: true,      // Automatically close brackets
            extraKeys: {
                Tab: cm => this.replaceTabWithSpaces(cm), // Replace tab key press with spaces
                "Enter": function(cm) {
                    var cursor = cm.getCursor();
                    var line = cm.getLine(cursor.line);
                    var currentIndent = line.match(/^\s*/)[0];  // Get current indentation level


                    if (cursor.ch === 0) {
                        var currentLine = cm.getLine(cursor.line);
                        var currentIndent = currentLine.match(/^\s*/)[0];
                        cm.replaceSelection("\n" + currentIndent);
                        return;
                    }

                    // Rest of your existing logic
                    if (line.trim() === '') {
                        var nextLine = cursor.line < cm.lineCount() - 1 ? cm.getLine(cursor.line + 1) : "";
                        var nextIndent = nextLine ? nextLine.match(/^\s*/)[0] : "";
                        
                        if (nextLine === "" || nextIndent.length < currentIndent.length) {
                            let reducedIndent = currentIndent.slice(0, Math.max(0, currentIndent.length - cm.getOption("indentUnit")));
                            cm.replaceSelection("\n" + reducedIndent);
                        } else {
                            cm.replaceSelection("\n" + currentIndent);
                        }
                    } else if (/:\s*$/.test(line)) {
                        cm.replaceSelection("\n" + currentIndent + Array(cm.getOption("indentUnit") + 1).join(" "));
                    } else {
                        cm.replaceSelection("\n" + currentIndent);
                    }
                },
                "Shift-Enter": function(cm) {
                    // Always create a new line with the same indentation as the current line
                    var cursor = cm.getCursor();
                    var line = cm.getLine(cursor.line);
                    var currentIndent = line.match(/^\s*/)[0];
                    cm.replaceSelection("\n" + currentIndent);
                },
                "Ctrl-.": "toggleComment",     // For Windows/Linux
                "Cmd-.": "toggleComment",       // For Mac

                "Backspace": function(cm) {
                    // Get cursor position
                    const cursor = cm.getCursor();
                    const line = cm.getLine(cursor.line);
                    
                    // Check if we're at an empty line with indentation
                    if (line.trim() === '' && cursor.ch > 0 && cursor.ch % 4 === 0) {
                        // Delete 4 spaces (one indentation level)
                        cm.replaceRange("", 
                            {line: cursor.line, ch: cursor.ch - 4}, 
                            {line: cursor.line, ch: cursor.ch});
                    } else {
                        // Normal backspace behavior
                        CodeMirror.commands.delCharBefore(cm);
                    }
                },
                    
            },

        });
    }


    async loadAddons() {
        // Only load addons if CodeMirror exists
        if (typeof CodeMirror === 'undefined') {
            console.error("CodeMirror not found! Addons will not be loaded.");
            return;
        }

        const addons = [
            'https://cdnjs.cloudflare.com/ajax/libs/codemirror/6.65.7/addon/edit/matchbrackets.min.js',
            'https://cdnjs.cloudflare.com/ajax/libs/codemirror/6.65.7/addon/edit/closebrackets.min.js',
            'https://cdnjs.cloudflare.com/ajax/libs/codemirror/6.65.7/addon/comment/comment.min.js',
        ];

        const loadScript = (src) => {
            return new Promise((resolve, reject) => {
                const script = document.createElement('script');
                script.src = src;
                script.onload = resolve;
                script.onerror = reject;
                document.head.appendChild(script);
            });
        };

        for (const addon of addons) {
            try {
                await loadScript(addon);
                console.log(`Loaded: ${addon}`);
            } catch (error) {
                console.error(`Failed to load: ${addon}`, error);
            }
        }
    }

    /**
     * Replaces the tab key press with spaces for consistent indentation.
     * @param {Object} cm - The CodeMirror instance.
     */
    replaceTabWithSpaces(cm) {
        let spaces = Array(cm.getOption("indentUnit") + 1).join(" ");
        cm.replaceSelection(spaces);
    }

    /**
     * Dynamically determines and applies the current theme based on user preference.
     * @returns {string} - The theme name to be applied.
     */
    getCurrentTheme() {
        const mode = document.documentElement.getAttribute('data-mode');
        const lightTheme = "github-light";
        const darkTheme = "github-dark-high-contrast";

        if (mode === 'dark') {
            return darkTheme;
        } else if (mode === 'light') {
            return lightTheme;
        } else if (mode === 'auto') {
            const prefersDarkScheme = window.matchMedia('(prefers-color-scheme: dark)').matches;
            return prefersDarkScheme ? darkTheme : lightTheme;
        }
    }

    /**
     * Sets up a listener to dynamically update the theme when the user changes it.
     */
    setupThemeListener() {
        const observer = new MutationObserver(mutations => {
            mutations.forEach(mutation => {
                if (mutation.attributeName === 'data-mode') {
                    this.editor.setOption('theme', this.getCurrentTheme());
                }
            });
        });

        observer.observe(document.documentElement, {
            attributes: true,
            attributeFilter: ['data-mode'],
        });

        // Set the initial theme when the editor is first initialized
        this.editor.setOption('theme', this.getCurrentTheme());
    }

    /**
     * Adds a custom overlay for highlighting specific comments for 
     * Supports # TODO, # FIKS MEG, # FYLL INN, # NOTE, # FIKSMEG, # IGNORER
     * @returns {Object} - The overlay mode configuration for CodeMirror.
     */
    addCommentOverlay(editor) {
        editor.addOverlay({
            token: function(stream) {
                const keywords = [
                    "# TODO", 
                    "# FIKSMEG", 
                    "# FIKS MEG", 
                    "# NOTE", 
                    "# FYLL INN", 
                    "# IGNORER", 
                    "# IKKE RØR",
                    "# FOKUS",
                    "# FORKLARING",
                    "# <--",
                    "# MERK",
                    "????",
                ];

                for (const keyword of keywords) {
                    if (stream.match(keyword)) {
                        return keyword.replace("# ", "").toLowerCase().replace(" ", "").replace(/\?+/g, "question");
                    }
                }
                
                while (stream.next() != null && !keywords.some(keyword => stream.match(keyword, false))) {}
                return null;
            }
        });
        return editor;
    }

    /**
     * Sets the code in the editor to a specified value.
     * @param {string} code - The code to set in the editor.
     */
    setValue(code) {
        this.editor.setValue(code);
    }

    /**
     * Gets the current value (code) from the editor.
     * @returns {string} - The code currently in the editor.
     */
    getValue() {
        return this.editor.getValue();
    }

    /**
     * Clears the editor content and optionally resets it to its initial value.
     * @param {string} [initialValue=""] - The initial code value to reset the editor to (optional).
     */
    resetEditor(initialValue = "") {
        this.editor.setValue(initialValue);
    }

    /**
     * Highlights a specific line in the editor (useful for debugging or showing errors).
     * @param {number} line - The line number to highlight (0-indexed).
     */
    highlightLine(line) {
        console.log("Highlighting line", line);
        this.editor.addLineClass(line, "background", "cm-highlight");
    }

    removehighlightLine(line) {
        this.editor.removeLineClass(line, "background", "line-highlight-red");
    }

    clearLineHighlights() {
        for (let i = 0; i < this.editor.lineCount(); i++) {
            this.editor.removeLineClass(i, "background", "cm-highlight");
        }
    }

    /**
     * Scrolls the editor to a specified line, useful for showing errors or results.
     * @param {number} line - The line number to scroll to (0-indexed).
     */
    scrollToLine(line) {
        this.editor.scrollIntoView({ line: line, ch: 0 }, 200);
    }

    refreshOnVisibilityChange() {
        const editorElement = this.editor.getWrapperElement();
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    this.editor.refresh();
                }
            });
        }, { threshold: 0.1 });
    
        observer.observe(editorElement);
    }
}