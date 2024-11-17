function bomb(x,y,board){
      for(let i = 0; i<8;i++){
            nx = x + dx[i];
            ny = y + dy[i];
            if(nx >= board.length || nx < 0 || ny >=board.length || ny<0) continue
            if (board[nx][ny] === 0){
                console.log(nx,ny)
                board[nx][ny] = 2;
            }
        }
}

function solution(board) {
    dx = [1,0,-1,0,1,1,-1,-1];
    dy = [0,1,0,-1,1,-1,-1,1];
    
    for(let i = 0;i<board.length;i++){
        for(let j = 0;j<board.length;j++){
            if(board[i][j] == 1)
                bomb(i,j,board);
        }
    }
   var answer = 0;
    board.forEach((e)=>answer+= e.filter((e2)=>e2 == 0).length)
    
    
    return answer;
}