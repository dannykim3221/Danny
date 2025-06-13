import tkinter as tk
from tkinter import ttk, messagebox
import os

class vocaList:
    def __init__(self):
        self.win = tk.Tk()
        self.win.title('단어장')

        self.voca = {}

        if os.path.exists('words.txt'):
            with open('words.txt', 'r', encoding='utf-8') as file:
                for line in file:
                    if ':' in line:
                        word, meaning = line.strip().split(':', 1)
                        self.voca[word] = meaning

    
        self.__buildGUI()



    def __buildGUI(self):
        text_label1 = ttk.Label(self.win, text='단어:', width=15, anchor='e')
        text_label2 = ttk.Label(self.win, text='뜻:', width=15, anchor='e')

        text_label1.grid(row=0, column=0)
        text_label2.grid(row=1, column=0)

        voca_group = ttk.Frame(self.win)
        self.word = tk.StringVar()
        inputW_entry = ttk.Entry(voca_group, textvariable=self.word)
        s_btn = ttk.Button(voca_group, text='검색', command=self.search)
        a_btn = ttk.Button(voca_group, text='추가', command=self.add)

        inputW_entry.pack(side='left')
        s_btn.pack(side='left')
        a_btn.pack(side='left')
        voca_group.grid(row=0, column=1)

        self.meaning = tk.StringVar()
        self.inputM_entry = ttk.Entry(self.win, textvariable=self.meaning)

        self.inputM_entry.grid(row=1, column=1, sticky='nswe')

        r_btn = ttk.Button(self.win, text='초기화', command=self.reset)
        r_btn.grid(row=2, column=0)

        btn_group = ttk.Frame(self.win)
        d_btn = ttk.Button(btn_group, text='삭제', command=self.delete)
        e_btn = ttk.Button(btn_group, text='종료', command=self.end)

        d_btn.pack(side='left')
        e_btn.pack(side='left')
        btn_group.grid(row=2, column=1, sticky='w')

    def search(self):
        word = self.word.get()
        if word in self.voca:
            self.meaning.set(self.voca[word])
        else:
            messagebox.showinfo('검색 오류', f'{word}란 단어는 없습니다!')
                
    def add(self):
        word = self.word.get()
        meaning = self.meaning.get()
        self.voca[word] = meaning
        messagebox.showinfo('추가 확인', f'단어 {word}를 추가했습니다.')
        self.word.set('')
        self.meaning.set('')
        print(self.voca)

    def reset(self):
        self.word.set('')
        self.meaning.set('')

    def end(self):
        with open('words.txt', 'w', encoding='utf-8') as file:
            for word, meaning in self.voca.items():
                file.write(f'{word}:{meaning}\n')
        self.win.destroy()

    def delete(self):
        word = self.word.get()
        if word in self.voca:
            del self.voca[word]
            messagebox.showinfo('단어 삭제', f'단어 {word}가 삭제되었습니다.')
            print(self.voca)
        else:
            messagebox.showinfo('단어 삭제', f'단어 {word}는 존재하지 않습니다.')
        self.word.set('')


voca = vocaList()
voca.win.mainloop()
