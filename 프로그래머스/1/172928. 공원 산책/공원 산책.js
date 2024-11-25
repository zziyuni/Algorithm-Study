function check(a,na,b,nb,park){
    if(na>=park.length || na<0 || nb>=park[0].length || nb < 0)
        return false;
    for(let i=Math.min(a,na);i<=Math.max(a,na);i++){
        for(let j =Math.min(b,nb);j<=Math.max(b,nb);j++){
            if(park[i][j] == "X"){
                return false;
            }
        }
    }
    return true;
}

function solution(park, routes) {
    park = park.map((e)=>e.split(''));
    var x,y;
    park.forEach((e,index)=>{if(e.indexOf("S") != -1){
      x =index;
      y = e.indexOf("S")
   }});
    var nx = 0;
    var ny = 0;
   routes.forEach((e)=>{
       var dir= e.split(' ')[0];
       var cnt =parseInt(e.split(' ')[1]);
       if(dir == "S"){
           nx= x+cnt;
           ny = y;
       }else if (dir == "N"){
           nx= x-cnt;
           ny = y;
       }else if(dir == "E"){
           ny= y+cnt;
           nx = x;
           
       }else if(dir == "W"){
           ny= y-cnt;  
           nx = x;

       }
       if(check(x,nx,y,ny,park)){
           x=nx;
           y=ny;
       }
       
   })
    return [x,y];
}