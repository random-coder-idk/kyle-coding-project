<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Catch the Box Game</title>
<style>
    body {
        font-family: Arial, sans-serif;
        text-align: center;
        background: #1e1e2f;
        color: white;
    }

    h1 {
        margin-top: 20px;
    }

    #gameArea {
        width: 400px;
        height: 400px;
        margin: 20px auto;
        background: #2c2c44;
        position: relative;
        border-radius: 10px;
        overflow: hidden;
    }

    #box {
        width: 50px;
        height: 50px;
        background: #ff4d4d;
        position: absolute;
        border-radius: 8px;
        cursor: pointer;
        transition: top 0.2s, left 0.2s;
    }

    #gui {
        margin-top: 10px;
    }

    button {
        padding: 10px 20px;
        border: none;
        border-radius: 5px;
        background: #4CAF50;
        color: white;
        font-size: 16px;
        cursor: pointer;
    }

    button:hover {
        background: #45a049;
    }
</style>
</head>
<body>

<h1>Catch the Box 🎯</h1>

<div id="gameArea">
    <div id="box"></div>
</div>

<div id="gui">
    <p>Score: <span id="score">0</span></p>
    <p>Time: <span id="time">20</span>s</p>
    <button onclick="startGame()">Start Game</button>
</div>

<script>
let score = 0;
let timeLeft = 20;
let gameInterval;
let moveInterval;

const box = document.getElementById("box");
const scoreDisplay = document.getElementById("score");
const timeDisplay = document.getElementById("time");
const gameArea = document.getElementById("gameArea");

box.addEventListener("click", () => {
    score++;
    scoreDisplay.textContent = score;
    moveBox();
});

function moveBox() {
    const maxX = gameArea.clientWidth - box.clientWidth;
    const maxY = gameArea.clientHeight - box.clientHeight;

    const x = Math.random() * maxX;
    const y = Math.random() * maxY;

    box.style.left = x + "px";
    box.style.top = y + "px";
}

function startGame() {
    score = 0;
    timeLeft = 20;
    scoreDisplay.textContent = score;
    timeDisplay.textContent = timeLeft;

    moveBox();

    clearInterval(gameInterval);
    clearInterval(moveInterval);

    gameInterval = setInterval(() => {
        timeLeft--;
        timeDisplay.textContent = timeLeft;

        if (timeLeft <= 0) {
            clearInterval(gameInterval);
            clearInterval(moveInterval);
            alert("Game Over! Your score: " + score);
        }
    }, 1000);

    moveInterval = setInterval(moveBox, 800);
}
</script>

</body>
</html>
