
// Disclamer: we are heavily inspired by HACK.lu's "Baby.js"

const firstFlag = process.env.first || 'KID20{fake_flag_1}'
const flag = process.env.flag || 'KID20{fake_flag_2}'

const flagObj = { flag: `Great job, your flag is: ${flag}` }

const readline = require('readline');

const failed = (msg) => { console.log(`${msg} failed`); process.exit(1) }
const assert = (msg, condition) => condition ? passed(msg) : failed(msg)
const passed = (num) => console.log(`Check ${num} passed`)

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rl.question('How can we help you?: ', (inp) => {
    let json
    try {
        json = JSON.parse(inp)
    } catch (e) {
        failed('Format failed: ' + e)
    }

    let { a, b, c, d, e, f, g, h, i, j, l, m } = json;
    assert(0, a * b != a * b)
    a = a * b
    assert(1, typeof a == 'number')
    assert(2, typeof b == 'number')
    assert(3, (a + b > b) == false)
    assert(4, (a + b < b) == false)
    assert(5, (a + b == b) == false)
    assert(6, c != 0)
    assert(7, Number(c) + Number(c) == c)
    assert(8, typeof c === 'string')
    assert(9, typeof Number(c) === 'number')
    assert(10, typeof d === 'number')
    assert(11, typeof e === 'number')
    assert(12, d === e)
    assert(13, 1 / d !== 1 / e)
    console.log(`Great, you found our first flag: ${firstFlag}, keep going!`)
    assert(14, typeof f === 'string')
    assert(15, typeof g === 'string')
    assert(16, g !== f)
    assert(17, Number(f) === Number(g))
    assert(18, (h < i) == true);
    assert(19, (i - h < 0) == true);

    assert(20, !j.includes('console'))
    assert(21, !m.includes('console'))
    assert(22, !j.includes("process"))
    assert(23, !m.includes("process"))
    assert(24, !j.includes("stdout"))
    assert(25, !m.includes("stdout"))
    assert(26, !j.includes("write"))
    assert(27, !m.includes("write"))
    let x = eval(m)    
    console.log(x[eval(j)[l](x)])
    rl.close()
})

