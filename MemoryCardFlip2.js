function chk(){
    if(true){
      shows[0].style.animation="opa 500ms ease forwards";
      shows[1].style.animation="opa 500ms ease forwards";
      complete+=2;
      if(complete>=16){
        result();
        clearInterval(counterHandle);
      }
      document.getElementById("wall").style.display="none";
    }else{
      shows[0].removeAttribute('style')
      shows[1].removeAttribute('style')
      document.getElementById("wall").style.display="block";
      ani[0]=setInterval(fade,25,shows[0],0)
      ani[1]=setInterval(fade,25,shows[1],1)
    }
     shows.length=0;
  }
  
  function timeCounter(){
    if(timer<0){
      document.getElementById('counter').style.width="0%";
      clearInterval(counterHandle);
      result();  //計時結束時執行結果判定函式
    }else{
      timer-=1;
      counterWidth-=0.001
      document.getElementById('counter').style.width=counterWidth+"%";
    }
  }