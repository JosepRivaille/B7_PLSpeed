var start = new Date().getTime();
var v = [];
var num = Math.floor(Math.random()*(9999999));

for (var i = 0; i < 9999999; ++i) v.push(i);

function dichotomic_search(x, v, l, r){
	while (l <= r) {
		var m = (l+r)/2;
		if (v[m] == x) return m;
		else if (v[m] < x) l = m+1;
		else r =  m-1;
	}
	return -1;
}

var pos = dichotomic_search(num, v, 0, v.length - 1);

var end = new Date().getTime();

console.log('--- '+(end-start)/1000+' seconds ---');

