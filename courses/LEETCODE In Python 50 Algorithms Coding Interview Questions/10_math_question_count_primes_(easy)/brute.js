
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
    let count = 0
    let primes = []
    for (let i = 2; i < length; i++) {
        let isPrime = true
        for (let j = 2; j < i; j++) {
            if (i % j === 0) {
                isPrime = false
            }
        }
        if (isPrime) {
            primes.push(i)
            count++
        }
        if (count === num) break
    }
    
    return primes
}
