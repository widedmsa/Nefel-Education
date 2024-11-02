/*
Steps :
1-  first we check if the amount entered by the user if it's equal to 0 the funtion will automatically return the word given by the user 
2- else , we check if the amount is bigger than the length of the word . if so, the amount will get the amount minus the length of the word 
3- we loop through the word from the end to the amount 
4- while we iterate through the word ,the last character of the word will be transferred to beginning of the word itself 
5- then we delete the last character that has been rotated 
6- lastly, the function will return the rotated word 
*/


function rotateStr(str,amnt){
    if (amnt==0){
        return str ;
    }
    else if(amnt >str.length) {
        amnt =amnt%str.length

    }
    for(var i =str.length-1;i>str.length-1-amnt;i--) {
        var temp=str[i];
        for(var j=str.length-1;j>0;j--){
            str[j]=str[j-1];
        }
        str[0]=temp;
    }
    return str
}
console.log(rotateStr("hello world",4))