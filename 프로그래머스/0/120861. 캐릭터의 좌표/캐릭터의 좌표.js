function solution(keyinput, board) {
 
    const move = {
        "up": [0,1],
        "down":[0,-1],
        "left":[-1,0],
        "right":[1,0],
    };
    
    let x = 0;
    let y = 0;
  
    keyinput.forEach((e)=>{
if(x+move[e][0] <= Math.floor(board[0]/2) && x+move[e][0] >= -Math.floor(board[0]/2) && y + move[e][1] <= Math.floor(board[1]/2) && y + move[e][1] >= -Math.floor(board[1]/2) ){
        x+= move[e][0];
        y+= move [e][1];}
        
    })
    return [x,y];
}