function fact(num) {
    var rval=1;
    for (var i = 2; i <= num; i++)
        rval = rval * i;
    return rval;
}

function comb(n, k) {
    if (k > n || k < 0) { return 0 }
    return fact(n) / (fact(k) * fact(n - k))
}

function matrixM(n) {
    let K = []
    const N = 2**-n
    for (let k = 0; k < n + 1; k++) {
        let row = []
        for (let l = 0; l < n + 1; l++) {
            let sum = 0
            for (let j = 0; j < n + 1; j++) {
                sum += comb(l, j) * comb(n - l, k - j) * 3**(k-j) * (-1)**j * N
            }
            row.push(sum)
        }
        K.push(row)
    }
    return K
}

function matrixM_(n) {
    let K = []
    for (let k = 0; k < n + 1; k++) {
        let row = []
        for (let l = 0; l < n + 1; l++) {
            if (l == n - k) { row.push(1) }
            else { row.push(0) }
        }
        K.push(row)
    }
    return K
}

function matrixM__(n) {
    let K = [];
    for (let k = 0; k < n + 1; k++) {
        let row = [];
        for (let l = 0; l < n + 1; l++) {
            if (l != k) { row.push(0); }
            else if ((n - l + 1) % 2) { row.push(1); }
            else { row.push(-1); }
        }
        K.push(row);
    }
    return K;
}

function matrixT__1(n) {
    let K = matrixM(n)
    for (let k = 0; k < n + 1; k++) {
        if (k % 2 == 0) { continue; }
        for (let l = 0; l < n + 1; l++) {
            K[k][l] *= -1
        }
    }
    return K;
}

function matrixT__(n) {
    let K = matrixM(n)
    for (let k = 0; k < n + 1; k++) {
        if (k % 2 == 0) { continue; }
        for (let l = 0; l < n + 1; l++) {
            K[l][k] *= -1
        }
    }
    return K;
}

function matrixT_(n) {
    let K = []
    for (let k = 0; k < n + 1; k++) {
        let row = []
        for (let l = 0; l < n + 1; l++) {
            row.push(comb(n - l, n - k) / comb(n, k) * 2**(n - k)) 
        }
        K.push(row)
    }
    return K
}

function matrixT_1(n) {
    let K = []
    for (let k = 0; k < n + 1; k++) {
        let row = []
        for (let l = 0; l < n + 1; l++) {
            row.push(comb(n - l, k - l) * comb(n, l) / 2**(n - l) * (-1)**(k + l))
        }
        K.push(row)
    }
    return K
}

function matrixT___(n) {
    let K = []
    const N = 2**-n
    for (let k = 0; k < n + 1; k++) {
        let row = []
        for (let l = 0; l < n + 1; l++) {
            let sum = 0
            let k_ = n - k
            for (let j = 0; j < n + 1; j++) {
                sum += comb(l, j) * comb(n - l, k_ - j) * (-1)**j * comb(n, l) * N
            }
            row.push(sum)
        }
        K.push(row)
    }
    return K
}

function matrixT___1(n) {
    let K = []
    for (let k = 0; k < n + 1; k++) {
        let row = []
        for (let l = 0; l < n + 1; l++) {
            let sum = 0
            let l_ = n - l
            for (let j = 0; j < n + 1; j++) {
                sum += comb(l_, j) * comb(n - l_, k - j) * (-1)**j / comb(n, k)
            }
            row.push(sum)
        }
        K.push(row)
    }
    return K
}
function linearNorm(x) { return x; }
function logNorm(x) { return Math.log(x); }
function symlogNorm(x, base=10, threshold=1, linscale=1) { 
    const c = linscale / (1 - 1 / base);
    let log_base = Math.log(base);
    if (x == 0) { return 0.; }
    let abs = Math.abs(x)
    if (abs <= threshold) { return x * c; }
    return Math.sign(x) * threshold * (c + Math.log(abs / threshold) / log_base)
}


const cool_white_warm_map = [
    [0.23046875, 0.296875  , 0.75      ],
    [0.265625  , 0.3515625 , 0.796875  ],
    [0.30078125, 0.40625   , 0.83984375],
    [0.33984375, 0.45703125, 0.87890625],
    [0.3828125 , 0.5078125 , 0.9140625 ],
    [0.421875  , 0.5546875 , 0.94140625],
    [0.46484375, 0.6015625 , 0.96484375],
    [0.5078125 , 0.64453125, 0.98046875],
    [0.55078125, 0.6875    , 0.9921875 ],
    [0.59375   , 0.72265625, 0.99609375],
    [0.63671875, 0.7578125 , 0.99609375],
    [0.68506052, 0.79136302, 0.99609375],
    [0.73606928, 0.83207831, 0.99609375],
    [0.79197618, 0.86954086, 0.99609375],
    [0.85379464, 0.90820313, 0.99609375],
    [0.92246943, 0.94845448, 0.99609375],
    [0.99609375, 0.99609375, 0.99609375],
    [0.99609375, 0.93954694, 0.90909866],
    [0.99335938, 0.88813063, 0.82920253],
    [0.98945313, 0.83754538, 0.75953871],
    [0.984375  , 0.7875    , 0.69508929],
    [0.98046875, 0.7422982 , 0.63512146],
    [0.97460938, 0.69840429, 0.58397647],
    [0.96757812, 0.65027518, 0.52883825],
    [0.95859375, 0.60501409, 0.48322554],
    [0.94140625, 0.55078125, 0.43359375],
    [0.921875  , 0.49609375, 0.38671875],
    [0.89453125, 0.4375    , 0.34375   ],
    [0.8671875 , 0.375     , 0.30078125],
    [0.83203125, 0.3125    , 0.2578125 ],
    [0.79296875, 0.2421875 , 0.21875   ],
    [0.75      , 0.15625   , 0.18359375],
    [0.703125  , 0.015625  , 0.1484375 ]
]

let green_white_yellow_map = [
    [0.91 , 0.729, 0.282],
    [1.0  , 1.0  , 1.0  ],
    [0.321, 0.729, 0.431]
]
    
function writeMatrixToCanvas(ctx, matrix, map, norm) {
    const n = matrix.length - 1
    const imageData = ctx.createImageData(n + 1, n + 1);
    const data = imageData.data;
    let absmax = Math.max(...matrix.flat().map(Math.abs))

    let normFunction = symlogNorm
    if (norm == "linear") { normFunction = linearNorm }
    else if (norm == "symlog") { normFunction = symlogNorm }

    let normalizedArr = normalize(matrix.flat(), normFunction, x0=-absmax, x1=absmax)
    let coloredArr = normalizedArr.map((x) => colorize(x, map))
    for (let i = 0; i < coloredArr.length; i++) {
        data[4 * i] = coloredArr[i][0] * 255;
        data[4 * i + 1] = coloredArr[i][1] * 255;
        data[4 * i + 2] = coloredArr[i][2] * 255;
        data[4 * i + 3] = 255;
    }
    ctx.putImageData(imageData, 0, 0);
}

function normalize(arr, norm, x0=null, x1=null) {
    if (x0 == null){ x0 = Math.min(...arr); }
    if (x1 == null){ x1 = Math.max(...arr); }
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
    function add_vector(a,b){
        return a.map((e, i) => e + b[i]);
    }
    return add_vector(clr1.map((v) => v * (1 - t)) , clr2.map((v) => v * t));
}



function MatrixSpec(name, generator, map) {
    this.name = name
    this.generator = generator
    this.map = map
    this.matrix = undefined
}

let matrices = [
    new MatrixSpec("M", matrixM, cool_white_warm_map),
    new MatrixSpec("M_", matrixM_, green_white_yellow_map),
    new MatrixSpec("M__", matrixM__, green_white_yellow_map),
    new MatrixSpec("T_", matrixT_, cool_white_warm_map),
    new MatrixSpec("T_1", matrixT_1, cool_white_warm_map),
    new MatrixSpec("T__", matrixT__, cool_white_warm_map),
    new MatrixSpec("T__1", matrixT__1, cool_white_warm_map),
    new MatrixSpec("T___", matrixT___, cool_white_warm_map),
    new MatrixSpec("T___1", matrixT___1, green_white_yellow_map),
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
    let MML = "http://www.w3.org/1998/Math/MathML";

    let root = document.createElementNS(MML, "msup");

    let symb = document.createElementNS(MML, "mi");
    symb.appendChild(document.createTextNode(name[0]));
    
    let exponent = document.createElementNS(MML, "mrow");

    for (let i = 0; i < name.split("_").length - 1; i++) {
        let prime = document.createElementNS(MML, "mi");
        prime.appendChild(document.createTextNode("&#x2032;"))
        exponent.appendChild(prime)
    }

    if (name.includes("1")) {
        let one = document.createElementNS(MML, "mn");
        one.appendChild(document.createTextNode("1"));

        let minus = document.createElementNS(MML, "mo");
        minus.appendChild(document.createTextNode("-"));

        exponent.appendChild(minus)
        exponent.appendChild(one)
    }
    
    root.appendChild(symb);
    root.appendChild(exponent);

    return root;
}

let hovered_canvas = null


window.addEventListener("load", function() { 
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
                var MML = "http://www.w3.org/1998/Math/MathML";
                var math = document.createElementNS(MML, "math");
                math.appendChild(matrix_name_to_math(matrix.name));
                output_matrix_name.innerHTML = math.outerHTML
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
        console.log(n)
        if (!isNaN(n) && n > 150) {
            document.getElementById("input-warning").style.display = "block";
        } else {
            document.getElementById("input-warning").style.display = "none";
        }
    });
})



