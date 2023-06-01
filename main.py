import tkinter as tk
from pathlib import Path

from utils import find_file, format_result


def display_files():
    # delete previous results
    txt_result.delete('0.0', tk.END)

    # get path and filename from form
    path = Path(ent_path.get())
    filename = ent_filename.get()

    # inserts formatted results into text box
    txt_result.insert('0.0', format_result(find_file(path, filename)))


window = tk.Tk()
window.title('File Searching Tool')

window.rowconfigure(0, weight=0)
window.rowconfigure(1, weight=1)

# Search frame
frm_form = tk.Frame(relief=tk.SUNKEN, borderwidth=3)
frm_form.grid(row=0, pady=10, padx=10, sticky='nsew')

# Search form
lbl_path = tk.Label(master=frm_form, text='Search path:')
ent_path = tk.Entry(master=frm_form, width=100)

lbl_path.grid(row=0, column=0, pady=5, padx=2, sticky='e')
ent_path.grid(row=0, column=1, pady=5, padx=2)

lbl_filename = tk.Label(master=frm_form, text='Filename:')
ent_filename = tk.Entry(master=frm_form, width=50)

lbl_filename.grid(row=1, column=0, pady=5, padx=2, sticky='e')
ent_filename.grid(row=1, column=1, pady=5, padx=2, sticky='w')

btn_search = tk.Button(master=frm_form, relief=tk.RAISED, width=20, text='Search', command=display_files)
btn_search.grid(row=2, column=1, pady=5, padx=2, sticky='w')

# Results frame
lbl_frm_result = tk.LabelFrame(master=window, relief=tk.SUNKEN, text='Search Results', padx=10, pady=10)
txt_result = tk.Text(master=lbl_frm_result, width=130, height=10)

lbl_frm_result.rowconfigure(0, weight=2)
lbl_frm_result.columnconfigure(0, weight=2)

lbl_frm_result.grid(row=1, pady=10, padx=10, sticky='nsew')
txt_result.grid(row=0, column=0, sticky='nsew')


if __name__ == '__main__':
    window.mainloop()
