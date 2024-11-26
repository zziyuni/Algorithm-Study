function solution(wallpaper) {
 
    let [lux,luy,rdx,rdy] = [Infinity,Infinity,0,0];
    
       wallpaper.forEach((e,index)=>{if(e.indexOf('#')!==-1){
        lux = Math.min(lux,index);
        luy = Math.min(luy,e.indexOf('#'));
        rdx = Math.max(rdx,index+1);
        rdy = Math.max(rdy,e.lastIndexOf('#')+1);
    }}) 
    
    return [lux,luy,rdx,rdy];
}