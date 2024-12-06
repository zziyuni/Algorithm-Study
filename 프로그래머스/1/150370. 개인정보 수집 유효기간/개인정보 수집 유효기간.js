function calc_date(today, term){
    var [year,month,day] = today.split('.').map(Number);
    month -= term
    
    if(month < 1 ){
       year -= month % 12 === 0? Math.abs(month) / 12 + 1 : Math.ceil(Math.abs(month) / 12);
        month = 12 + (month) %12;
    }
    return `${year}.${String(month).padStart(2, '0')}.${String(day).padStart(2, '0')}`;
}

function solution(today, terms, privacies) {
    var answer = [];
    var type_date = {};
   
    terms.forEach((e)=>{
        type_date[e.split(' ')[0]]=calc_date(today,parseInt(e.split(' ')[1]))
    });
    
    privacies.forEach((e,index)=>{
        [date, type] = e.split(' ')
        if(type_date[type] >= date){
            answer.push(index+1);
        }
    })
    return answer;
}