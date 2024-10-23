//first step is to create a function with two parametrs ("str1" and "str2") that will be entered by the user in order to compare them .
//second step is  to check whether the two strings have the same length or not : if the two strings don't have the same length the function will automatically exit console false. 
// else : if the two strings have the same length in this situation we convert both of them to upper case and we check if they have identical characters 
//if the  characters are identical the function will return true  

function compareStrings(str1,str2){
    str1.toUpperCase()
    str2.toUpperCase()
    if (str1.length !== str2.length ) {
        console.log(false) ;
    }

    else {
        if (str1.toUpperCase() === str2.toUpperCase()) {
            console.log(true) ;
        }
    }
    
}
var result = compareStrings("hello","goodMorning") ;
console.log(result) ;
