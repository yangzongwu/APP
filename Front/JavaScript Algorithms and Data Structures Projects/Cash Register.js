function checkCashRegister(price, cash, cid) {
  var cid_obj=arrayToObj(cid);
  var gap=cash-price;
  var cur=[["ONE HUNDRED",100],["TWENTY",20],["TEN",10],["FIVE",5],
  ["ONE",1],["QUARTER",0.25],["DIME",0.1],["NICKEL",0.05],
  ["PENNY",0.01]]

  var result_last=[]
  var result_amount=0

  for(var i=0;i<cur.length;i++){
    var name=cur[i][0];
    var amount=cur[i][1];
    if(gap>amount && cid_obj.hasOwnProperty(name) && cid_obj[name]!=0){
      var total=0;
      while(gap>=amount && cid_obj[name]!=0){
        gap=parseFloat((gap-amount).toFixed(2));
        total=parseFloat((total+amount).toFixed(2));
        cid_obj[name]=parseFloat((cid_obj[name]-amount).toFixed(2));
      }
      result_last.push([name,total]);
      result_amount+=cid_obj[name];
    }
  }

  if(gap>0){
    return {status: "INSUFFICIENT_FUNDS", change: []};
  }else if(gap==0 && result_amount>0){
    return {status: "OPEN", change:result_last};
  }else{
    return {status: "CLOSED", change:cid};
  }


}

function arrayToObj(cid){
  var cid_obj={};
  for(var i=0;i<cid.length;i++){
    cid_obj[cid[i][0]]=cid[i][1];
  }
  return cid_obj;
}

// Example cash-in-drawer array:
// [["PENNY", 1.01],
// ["NICKEL", 2.05],
// ["DIME", 3.1],
// ["QUARTER", 4.25],
// ["ONE", 90],
// ["FIVE", 55],
// ["TEN", 20],
// ["TWENTY", 60],
// ["ONE HUNDRED", 100]]

checkCashRegister(19.5, 20, [["PENNY", 0.5], ["NICKEL", 0], ["DIME", 0], ["QUARTER", 0], ["ONE", 0], ["FIVE", 0], ["TEN", 0], ["TWENTY", 0], ["ONE HUNDRED", 0]]);
