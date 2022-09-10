import tkinter as tk


class ConfigDialog:
    def __init__(self, options: dict, display: dict = None, title: str = "Configuration"):
        super().__init__()
        self.window = None
        self._widgets = None

        self._title = title
        self._options = options
        self._display = {} if display is None else display

    def __getitem__(self, key) -> str:
        if self._widgets is None:
            return str(self._options[key])
        else:
            return self._widgets[key][1].get()

    def __setitem__(self, key, value):
        if self._widgets is None:
            self._options[key] = value
        else:
            self._widgets[key][1].delete(0, tk.END)
            self._widgets[key][1].insert(0, value)

    def spawn(self):
        self.window = tk.Toplevel()
        self.window.title(self._title)
        self.window.protocol('WM_DELETE_WINDOW', self._destroy_popup)
        self.window.resizable(width=False, height=False)

        self._widgets = {}
        for i, (k, v) in enumerate(self._options.items()):
            self._widgets[k] = [
                tk.Label(self.window, text=self._display.get(k, f"<{k}>")),
                tk.Entry(self.window)
            ]
            self._widgets[k][0].grid(row=i, column=0)
            self._widgets[k][1].grid(row=i, column=1)
            self._widgets[k][1].insert(0, v)

    def _destroy_popup(self):
        for k in self._widgets.keys():
            self._options[k] = self._widgets[k][1].get()

        self._widgets = None

        self.window.destroy()

        self.window = None
