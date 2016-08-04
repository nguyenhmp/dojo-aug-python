function rotate(arr, shiftBy){
	while (shiftBy > arr.length){
		shiftBy = shiftBy - arr.length
	}
	for ( var i = 0; i < shiftBy; i++){
		end = arr[arr.length-1]
		for (var k = arr.length - 1; k > 0; k--){
			arr[k] = arr[k-1]
		}
		arr[0] = end
	}
}

arr = [0,1,2,3,4]

rotate(arr, 3)
console.log(arr)k