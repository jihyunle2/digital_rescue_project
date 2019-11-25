import tkinter as tk

def func_enter(event):
    result = "댓글을 달기전에 한번 더 생각하셨나요?"
    print(result)
    display.delete(0,tk.END)  # 0번째 자리부터 끝까지 삭제하는 명령어
    display.insert(0,result)  # 결과 띄우기

def func_bs(event):
    result = "당신은 지금 누군가의 지울 수 없는 상처를 지워주고있습니다."
    print(result)
    display.delete(0,tk.END)  # 0번째 자리부터 끝까지 삭제하는 명령어
    display.insert(0,result)  # 결과 띄우기
 
def clear(event):
    display.delete(0,tk.END)

root = tk.Tk()
root.title("TEST DISPLAY")
root.geometry("400x100")

#입력 및 결과 표시창
display = tk.Entry(root, width=40)
display.grid(row=0, columnspan=2)

root.bind('<Escape>', clear)
root.bind('<Return>', func_enter) 
root.bind('<BackSpace>', func_bs) 
 
root.mainloop()

