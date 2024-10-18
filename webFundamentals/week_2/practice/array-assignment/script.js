// always hungry 
function findFood(arr){
    for(var i=0;i<arr.length;i++) {
        if (arr[i]=="food") {
            console.log("yummy") ;
    } else {
        console.log("hungry") ;
        }
    }
    return arr ;
    }
    findFood(["d","55","john","f"]) ;





// High pass filter 
function highPassFilter(arr,cutoff){
    var filteredArr = [] ;
    for (var i=0;i<arr.length;i++) {
        if (arr[i] > cutoff) {
            filteredArr.push(arr[i]) 
        }
    }
    return filteredArr ;
}
var result = highPassFilter([6,1,0,50,18,3],7);
console.log(result) ;



// better than average 
function betterThanAverage(arr) {
var sum = 0 ;
    for(var i = 0;i<arr.length;i++)
        sum+=arr[i];
}
var average = sum / arr.length ;
var count = 0 ;
    for(i = 0;i<arr.length;i++) {
        if (arr[i]>average) {
            count++
        }
    }



// Array reverse 
function reverseArr(arr){
var start = 0 ;
    for(var i =0;i<arr.length;i++) {
        arr[i] = arr[arr.length-1-i]
        arr[arr.length-1-i]=arr[start]
        start++

    }
return arr;
}
var result = reverseArr(["a","b","c","d"]) ;
console.log(result) ;

// Fibonacci array 
function fibonacci(n){
    var fibrArr=[0,1] ;
}