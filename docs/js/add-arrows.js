
window.addEventListener("load", function() { 
    let style_base = {
        color: "#777",
        size: 1,
        endPlugSize: 2,
        startPlugSize: 2,
    }

    function double_arrow(a, b) {
        new LeaderLine(
            document.getElementById("c-" + a),
            document.getElementById("c-" + b), 
            Object.assign({}, style_base, {startPlug: "arrow1"})
        );
    }

    function single_arrow(a, b) {
        new LeaderLine(
            document.getElementById("c-" + a),
            document.getElementById("c-" + b), 
            style_base
        );
    }

    double_arrow("a", "b")
    double_arrow("a_", "b_")
    double_arrow("a__", "b__")
   
    single_arrow("b", "b_")
    single_arrow("b_", "b__")

    single_arrow("a__", "a_")
    single_arrow("a_", "a")

    new LeaderLine(
        document.getElementById("c-" + "b"),
        document.getElementById("c-" + "b__"), 
        Object.assign({}, style_base, {startSocket: "right", endSocket: "right"})
    );
    

    new LeaderLine(
        document.getElementById("c-" + "a__"),
        document.getElementById("c-" + "a"), 
        Object.assign({}, style_base, {startSocket: "left", endSocket: "left"})
    );
});
