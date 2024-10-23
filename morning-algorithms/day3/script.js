// steps : 
// 1 we will receive data from the user which will be an array (which can be a set of numbers , strings , ...) and a seprataor (, -, + ..)
// 2 we will declare an empty container 
// 3 if the data  entered by the user contains only one element the function will return that element 
// 4 if the data entered by the user is empty the function will return an empty string (which is the empty container)
// 5 if the data  entered by the use r contains only one element the function will return that element
// 5 we will create a for  loop which will loop through the array from 0 to the length of the array minus 1
// 6 if the value of i is less than array.length-1 arr[.] will be transfered to the empty container along with the separator 
// 7 else only the element of the array will be transfered to the container without the separartor  
// 8 as the array reaches its end  we have to get it of the separator which was pushed at end of the array 
// 9 in this situation we will be using 


function join(array,separator){
    var empty = "" 
    if (array.length <1) {
        return empty 
    }
    elif (array.length =1) {
        empty = array 
    }
    else 
}