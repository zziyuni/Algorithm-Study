function solution(order) {
    
    return Array.from(order.toString()).filter((e)=>e != 0 && e%3 == 0).length;
}