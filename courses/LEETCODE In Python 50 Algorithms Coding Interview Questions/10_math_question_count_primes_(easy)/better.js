
/*  Given a number n, return an array of prime numbers whose
    size is equal to the number n. 

    Example: 
    0 -> [], 
    1 -> [2], 
    3 -> [2, 3, 5] 
*/

function getPrimes(num) {
    if (num === 0) {
        return []
    }
    if (num === 1) {
        return [2]
    }

    const length = num ** 2
    const isPrime = new Array(length).fill(true)
    isPrime[0] = false
    isPrime[1] = false
    let count = 0
    for (let i = 2; i < Math.ceil(Math.sqrt(length)); i++) {
        if (isPrime[i]) {
            for (let j = i * 2; j < length; j+= i) {
                isPrime[j] = false
            }
            count++
        }
        if (count === num) break
    }

    count = 0
    let primes = []
    for (let i = 0; i < length; i++) {
        if (isPrime[i]) {
            primes.push(i)
            count++
        }
        if (count === num) break
    }
    
    return primes
}
