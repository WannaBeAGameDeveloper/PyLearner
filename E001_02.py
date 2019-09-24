# 引入turtle库
import turtle

# 设置画笔的宽度和颜色
turtle.pensize(4)
turtle.pencolor('red')

# 绘制正方形
# forward方法使画笔沿当前画笔方向画一条直线，长度由参数指定
# right方法使画笔以当前位置和方向向右旋转一定角度，旋转角度由参数指定
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)

turtle.mainloop()
