function rot13(str) { // LBH QVQ VG!

  var rep={
    'A':'N','B':'O','C':'P','D':'Q','E':'R',
    'F':'S','G':'T','H':'U','I':'V','J':'W',
    'K':'X','L':'Y','M':'Z','N':'A','O':'B',
    'P':'C','Q':'D','R':'E','S':'F','T':'G',
    'U':'H','V':'I','W':'J','X':'K','Y':'L',
    'Z':'M',};

  var tmp=[];
  for(var i=0;i<str.length;i++){
    if(rep.hasOwnProperty(str[i])){
      tmp.push(rep[str[i]]);
    }else{
      tmp.push(str[i]);
    }
  }


  var res="";
  for(i=0;i<tmp.length;i++){
    res+=tmp[i];
  }


  return res;
}

// Change the inputs below to test
rot13("SERR CVMMN!");
