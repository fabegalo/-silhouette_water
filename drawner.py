import turtle,time

# draws a rectangle given top left position of a rectangle
def draw_filled_rectangle(board,x,y,width,height,size,color,fill):
  board.fillcolor(fill)
  board.pencolor(color)
  board.pensize(size)
  board.setheading(0)
 
  board.begin_fill()
  board.up()
  board.goto(x,y)
  board.down()
  # draw top
  board.forward(width)
  # draw right
  board.right(90)
  board.forward(height)
  # draw bottom
  board.right(90)
  board.forward(width)
  # draw left
  board.right(90)
  board.forward(height)
  board.end_fill()

def mount_water_silhouettes(silhouette, resultado):
   
    M = len(silhouette)
    N = max(silhouette)
    matriz = [[0] * N for _ in range(M)]

    for i in range(0, len(silhouette)):
        for y in range(0, max(silhouette)):

            tamanho = silhouette[i]

            if y < tamanho:
                matriz[i][y] = 'TORRE'
            else:
                matriz[i][y] = 'VAZIO'

    for i in range(0, len(silhouette)):
        agua = resultado[i]
        if agua != 0:
            y = 0
            while agua > 0:
                if matriz[i][y] == 'VAZIO':
                    matriz[i][y] = 'AGUA'
                    agua-=1
                y+=1

    # for line in matriz:
    #     print ('  '.join(map(str, line)))

    return matriz

def draw_silhouette(silhouettes, resultados):

    board = turtle.Turtle()

    turtle.tracer(False)

    turtle.speed(0)

    for i in range(0, len(silhouettes)):

        matriz = mount_water_silhouettes(silhouettes[i], resultados[i])

        row = len(matriz)
        columns = len(max(matriz))
        
        for x in range(0, row):
            for y in range(0, columns):
    
                if matriz[x][y] == 'VAZIO':
                    color = 'white'
                elif matriz[x][y] == 'TORRE':
                    color = 'gray'
                else:
                    color = 'blue'
                
                draw_filled_rectangle(board,-200+x*20,y*20,20,20,2,"black", color)

        turtle.update()
        time.sleep(2)
        board.clear()
    turtle.done()