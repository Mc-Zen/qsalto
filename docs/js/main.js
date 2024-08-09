function fact(num) {
    var rval = 1;
    for (var i = 2; i <= num; i++)
        rval = rval * i;
    return rval;
}

function comb(n, k) {
    if (k > n || k < 0) { return 0 }
    return fact(n) / (fact(k) * fact(n - k))
}

function comb(n, k) {
    let val = 1n
    for (let j = 1; j <= k; j++) {
        val *= BigInt(n + 1 - j)
        val /= BigInt(j)
    }
    return val
}

function matrix_M(n) {
    let K = []
    const N = 2 ** -n
    for (let i = 0; i < n + 1; i++) {
        let row = []
        for (let j = 0; j < n + 1; j++) {
            let sum = 0
            for (let l = 0; l < n + 1; l++) {
                sum += comb(n - j, i - l) * comb(j, l) * (-1) ** l * 3 ** (i - l) * N
            }
            row.push(sum)
        }
        K.push(row)
    }
    return K
}

function makeEmptyMatrix(n) {
    let K = []
    for (let i = 0; i < n; i++) {
        let row = Array(n)
        row.fill(0n)
        K.push(row)
    }
    return K
}

function matrix_M(n) {
    let K = makeEmptyMatrix(n + 1)
    for (let i = 0; i < n + 1; i++) {
        K[0][i] = 1n
        K[i][n] += comb(n, i) * BigInt((-1) ** i)
    }
    for (let i = 1; i < n + 1; i++) {
        for (let j = n - 1; j >= 0; j--) {
            K[i][j] = 3n * K[i - 1][j + 1] + K[i - 1][j] + K[i][j + 1]
        }
    }
    const N = 2 ** n
    for (let i = 0; i < n + 1; i++) {
        for (let j = 0; j < n + 1; j++) {
            K[i][j] = Number(K[i][j]) / N
        }
    }
    return K
}

function matrix_M1(n) {
    let K = []
    for (let i = 0; i < n + 1; i++) {
        let row = []
        for (let j = 0; j < n + 1; j++) {
            if (j == n - i) { row.push(1) }
            else { row.push(0) }
        }
        K.push(row)
    }
    return K
}

function matrix_M2(n) {
    let K = [];
    for (let i = 0; i < n + 1; i++) {
        let row = [];
        for (let j = 0; j < n + 1; j++) {
            if (j != i) { row.push(0); }
            else if ((n - j + 1) % 2) { row.push(1); }
            else { row.push(-1); }
        }
        K.push(row);
    }
    return K;
}

function matrix_iT2(n) {
    let K = matrix_M(n)
    for (let i = 0; i < n + 1; i++) {
        if (i % 2 == 0) { continue; }
        for (let j = 0; j < n + 1; j++) {
            K[i][j] *= -1
        }
    }
    return K;
}

function matrix_T2(n) {
    let K = matrix_M(n)
    for (let i = 0; i < n + 1; i++) {
        if (i % 2 == 0) { continue; }
        for (let j = 0; j < n + 1; j++) {
            K[j][i] *= -1
        }
    }
    return K;
}

function matrix_T1(n) {
    let K = makeEmptyMatrix(n + 1)
    for (let i = 0; i < n + 1; i++) {
        K[i][i] = 1n
        K[n][i] = 1n
    }
    for (let j = n - 1; j >= 0; j--) {
        for (let i = j - 1; i < n; i++) {
            if (i == -1) { continue }
            K[i][j] = K[i][j + 1] + K[i + 1][j + 1]
        }
    }
    for (let i = 0; i < n + 1; i++) {
        let N = 2 ** (n - i)
        let W = Number(K[i][0])
        for (let j = 0; j < n + 1; j++) {
            K[i][j] = Number(K[i][j]) * N / W
        }
    }
    return K
}

function matrix_iT1(n) {
    let K = makeEmptyMatrix(n + 1)
    for (let i = 0; i < n + 1; i++) {
        K[i][i] = 1n
        K[n][i] = 1n
    }
    for (let j = n - 1; j >= 0; j--) {
        for (let i = j - 1; i < n; i++) {
            if (i == -1) { continue }
            K[i][j] = K[i][j + 1] + K[i + 1][j + 1]
        }
    }
    for (let j = n; j >= 0; j--) {
        let N = 2 ** (j - n)
        let W = K[j][0]
        for (let i = 0; i < n + 1; i++) {
            K[i][j] = Number(K[i][j] * W) * N
        }
    }
    for (let j = 0; j < n + 1; j++) {
        for (let i = j + 1; i < n + 1; i += 2) {
            K[i][j] *= -1
        }
    }
    return K
}

function matrix_T3(n) {
    let K = makeEmptyMatrix(n + 1)
    for (let i = 0; i < n + 1; i++) {
        K[0][i] = BigInt((-1) ** i)
        K[i][0] = comb(n, i)
    }
    for (let i = 1; i < n + 1; i++) {
        for (let j = 1; j < n + 1; j++) {
            K[i][j] = K[i - 1][j - 1] - K[i - 1][j] - K[i][j - 1]
        }
    }
    const N = 2 ** n
    for (let j = 0; j < n + 1; j++) {
        let W = comb(n, j)
        for (let i = 0; i < n + 1; i++) {
            K[i][j] = Number(K[i][j] * W) / Number(N)
        }
    }
    return K
}

function matrix_iT3(n) {
    let K = makeEmptyMatrix(n + 1)
    for (let i = 0; i < n + 1; i++) {
        K[0][i] = 1n
        K[i][0] = comb(n, i) * BigInt((-1) ** i)
    }
    for (let i = 1; i < n + 1; i++) {
        for (let j = 1; j < n + 1; j++) {
            K[i][j] = K[i - 1][j - 1] + K[i - 1][j] + K[i][j - 1]
        }
    }
    for (let i = 0; i < n + 1; i++) {
        let W = comb(n, i)
        for (let j = 0; j < n + 1; j++) {
            K[i][j] = Number(K[i][j]) / Number(W)
        }
    }
    return K
}

function linearNorm(x) { return x; }
function logNorm(x) { return Math.log(x); }
function symlogNorm(x, base = 10, threshold = 1, linscale = 1) {
    const c = linscale / (1 - 1 / base);
    let log_base = Math.log(base);
    if (x == 0) { return 0.; }
    let abs = Math.abs(x)
    if (abs <= threshold) { return x * c; }
    return Math.sign(x) * threshold * (c + Math.log(abs / threshold) / log_base)
}


const cool_white_warm_map = [
    [0.23046875, 0.296875, 0.75],
    [0.265625, 0.3515625, 0.796875],
    [0.30078125, 0.40625, 0.83984375],
    [0.33984375, 0.45703125, 0.87890625],
    [0.3828125, 0.5078125, 0.9140625],
    [0.421875, 0.5546875, 0.94140625],
    [0.46484375, 0.6015625, 0.96484375],
    [0.5078125, 0.64453125, 0.98046875],
    [0.55078125, 0.6875, 0.9921875],
    [0.59375, 0.72265625, 0.99609375],
    [0.63671875, 0.7578125, 0.99609375],
    [0.68506052, 0.79136302, 0.99609375],
    [0.73606928, 0.83207831, 0.99609375],
    [0.79197618, 0.86954086, 0.99609375],
    [0.85379464, 0.90820313, 0.99609375],
    [0.92246943, 0.94845448, 0.99609375],
    [0.99609375, 0.99609375, 0.99609375],
    [0.99609375, 0.93954694, 0.90909866],
    [0.99335938, 0.88813063, 0.82920253],
    [0.98945313, 0.83754538, 0.75953871],
    [0.984375, 0.7875, 0.69508929],
    [0.98046875, 0.7422982, 0.63512146],
    [0.97460938, 0.69840429, 0.58397647],
    [0.96757812, 0.65027518, 0.52883825],
    [0.95859375, 0.60501409, 0.48322554],
    [0.94140625, 0.55078125, 0.43359375],
    [0.921875, 0.49609375, 0.38671875],
    [0.89453125, 0.4375, 0.34375],
    [0.8671875, 0.375, 0.30078125],
    [0.83203125, 0.3125, 0.2578125],
    [0.79296875, 0.2421875, 0.21875],
    [0.75, 0.15625, 0.18359375],
    [0.703125, 0.015625, 0.1484375]
]

let green_white_yellow_map = [
    [0.91, 0.729, 0.282],
    [1.0, 1.0, 1.0],
    [0.321, 0.729, 0.431]
]

function maxAbsElement(matrix) {
    let max = 0;
    for (let row of matrix) {
        max = Math.max(max, ...row.map(Math.abs))
    }
    return max
}

function writeMatrixToCanvas(ctx, matrix, map, norm) {
    const n = matrix.length - 1
    const imageData = ctx.createImageData(n + 1, n + 1);
    const data = imageData.data;
    let absmax = maxAbsElement(matrix)
    // let absmax = Math.max(...matrix.flat().map(Math.abs))

    let normFunction = symlogNorm
    if (norm == "linear") { normFunction = linearNorm }
    else if (norm == "symlog") { normFunction = symlogNorm }

    let normalizedArr = normalize(matrix.flat(), normFunction, x0 = -absmax, x1 = absmax)
    let coloredArr = normalizedArr.map((x) => colorize(x, map))
    for (let i = 0; i < coloredArr.length; i++) {
        data[4 * i] = coloredArr[i][0] * 255;
        data[4 * i + 1] = coloredArr[i][1] * 255;
        data[4 * i + 2] = coloredArr[i][2] * 255;
        data[4 * i + 3] = 255;
    }
    ctx.putImageData(imageData, 0, 0);
}

function normalize(arr, norm, x0 = null, x1 = null) {
    if (x0 == null) { x0 = Math.min(...arr); }
    if (x1 == null) { x1 = Math.max(...arr); }
    const y0 = 0;
    const y1 = 1;
    const a = (y1 - y0) / (norm(x1) - norm(x0));
    const b = -a * norm(x0) + y0;
    let trafo = (x) => a * norm(x) + b;
    return arr.map(trafo);
}

function colorize(x, map) {
    if (isNaN(x)) { return [1, 1, 1, 1]; }
    // x in [0, 1]
    const i = x * (map.length - 1);
    let i1 = (Math.floor(i));
    if (i1 == map.length - 1) {
        i1 -= 1;
    }
    const i2 = i1 + 1;
    const t = (i - i1);
    const clr1 = map[i1];
    const clr2 = map[i2];
    function add_vector(a, b) {
        return a.map((e, i) => e + b[i]);
    }
    return add_vector(clr1.map((v) => v * (1 - t)), clr2.map((v) => v * t));
}



function MatrixSpec(name, generator, map) {
    this.name = name
    this.generator = generator
    this.map = map
    this.matrix = undefined
}

let matrices = [
    new MatrixSpec("M", matrix_M, cool_white_warm_map),
    new MatrixSpec("M1", matrix_M1, green_white_yellow_map),
    new MatrixSpec("M2", matrix_M2, green_white_yellow_map),
    new MatrixSpec("T1", matrix_T1, cool_white_warm_map),
    new MatrixSpec("iT1", matrix_iT1, cool_white_warm_map),
    new MatrixSpec("T2", matrix_T2, cool_white_warm_map),
    new MatrixSpec("iT2", matrix_iT2, cool_white_warm_map),
    new MatrixSpec("T3", matrix_T3, cool_white_warm_map),
    new MatrixSpec("iT3", matrix_iT3, green_white_yellow_map),
]

function drawMatrix(n, name, matrix, map, norm) {
    var c = document.getElementById(name);
    c.width = n + 1
    c.height = n + 1
    writeMatrixToCanvas(c.getContext("2d"), matrix, map, norm);
}


function updateMatrices(n, norm) {
    if ("URLSearchParams" in window) {
        const url = new URL(window.location)
        url.searchParams.set("n", n.toString())
        history.pushState(null, "", url);
    }
    for (let matrix of matrices) {
        if (matrix.matrix == undefined || matrix.matrix.length - 1 != n) {
            matrix.matrix = matrix.generator(n);
        }
        drawMatrix(n, matrix.name, matrix.matrix, matrix.map, norm)
    }
}

function getSelectedNorm() {
    return document.querySelector('input[name="norm"]:checked').value
}

function matrix_name_to_math(name) {
    let inv = false
    if (name.includes("i")) {
        inv = true
        name = name.substr(1)
    }
    let letter = name.substr(0, 1)
    let num = parseInt(name.substr(1))

    let result = letter
    if (num == 2 || num == 3) {
        result = "\\tilde{" + result + "}"
    }
    if (num == 1 || num == 3) {
        result += "'"
    }
    if (inv) {
        result += "^{-1}"
    }
    console.log(result, num)
    return "\\(" + result + "\\)"
}

let hovered_canvas = null


window.addEventListener("load", function () {
    const input_n = document.getElementById("input_n")
    const output_matrix_value = document.getElementById("matrix_value")
    const output_matrix_name = document.getElementById("matrix_name")

    if ("URLSearchParams" in window) {
        const url = new URL(window.location)
        let a = url.searchParams.get("n")
        if (a != null) { input_n.value = a }
    }

    updateMatrices(parseInt(input_n.value), getSelectedNorm())

    const inputs = [input_n].concat(Array.from(document.querySelectorAll("[name=norm]")));
    for (const input of inputs) {
        input.addEventListener("change", (evt) => {
            return updateMatrices(parseInt(input_n.value), getSelectedNorm())
        });
    }

    function clamp(x, min, max) {
        return Math.min(max, Math.max(min, x))
    }

    for (const matrix of matrices) {
        const canvas = document.getElementById(matrix.name)
        canvas.addEventListener("mousemove", (evt) => {
            const bounds = canvas.getBoundingClientRect();
            const n = matrix.matrix.length - 1
            const x = clamp(Math.floor((evt.clientX - bounds.left) / bounds.width * canvas.width), 0, n + 1);
            const y = clamp(Math.floor((evt.clientY - bounds.top) / bounds.height * canvas.height), 0, n + 1);


            output_matrix_value.innerHTML = "[" + y + "," + x + "] = " + matrix.matrix[y][x].toString().replace("-", "−")

            if (hovered_canvas != canvas) {
                output_matrix_name.innerHTML = matrix_name_to_math(matrix.name)
                MathJax.typeset()
                hovered_canvas = canvas
            }
        });
    }

    document.getElementById("open-grid").addEventListener("click", (evt) => {
        document.getElementsByClassName("qwe-formulas")[0].style.display = "grid";
    });
    // output_matrix_value.innerHTML = ""


    input_n.addEventListener("input", (evt) => {

        let n = parseInt(input_n.value)

        if (!isNaN(n) && n > 350) {
            document.getElementById("input-warning").style.display = "block";
        } else {
            document.getElementById("input-warning").style.display = "none";
        }

        if (!isNaN(n) && n > 500) {
            input_n.value = 500
        }
    });
})



