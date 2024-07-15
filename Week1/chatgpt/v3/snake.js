// Constants
const canvas = document.getElementById('gameCanvas');
const ctx = canvas.getContext('2d');
const box = 20; // Size of each grid box
const canvasSize = 400; // Canvas width and height
const canvasBoxes = canvasSize / box; // Number of boxes in the canvas

// Initial snake setup
let snake = [];
snake[0] = { x: 10 * box, y: 10 * box };

// Initial food position
let food = generateFood();

// Initial direction
let direction = '';

// Event listener for keyboard input
document.addEventListener('keydown', directionHandler);

// Game over elements
const gameOverDiv = document.getElementById('gameOver');
const restartButton = document.getElementById('restartButton');
restartButton.addEventListener('click', restartGame);

// Function to handle direction changes
function directionHandler(event) {
    if (event.keyCode === 37 && direction !== 'RIGHT') {
        direction = 'LEFT';
    } else if (event.keyCode === 38 && direction !== 'DOWN') {
        direction = 'UP';
    } else if (event.keyCode === 39 && direction !== 'LEFT') {
        direction = 'RIGHT';
    } else if (event.keyCode === 40 && direction !== 'UP') {
        direction = 'DOWN';
    }
}

// Function to generate food at a random position
function generateFood() {
    return {
        x: Math.floor(Math.random() * (canvasBoxes - 1) + 1) * box,
        y: Math.floor(Math.random() * (canvasBoxes - 1) + 1) * box
    };
}

// Function to check for collisions
function collision(newHead, array) {
    for (let i = 0; i < array.length; i++) {
        if (newHead.x === array[i].x && newHead.y === array[i].y) {
            return true;
        }
    }
    return false;
}

// Function to draw the game elements
function draw() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    // Draw snake
    for (let i = 0; i < snake.length; i++) {
        ctx.fillStyle = (i === 0) ? 'green' : 'white';
        ctx.fillRect(snake[i].x, snake[i].y, box, box);
        ctx.strokeStyle = 'red';
        ctx.strokeRect(snake[i].x, snake[i].y, box, box);
    }

    // Draw food
    ctx.fillStyle = 'red';
    ctx.fillRect(food.x, food.y, box, box);

    // Move snake
    let snakeX = snake[0].x;
    let snakeY = snake[0].y;

    if (direction === 'LEFT') snakeX -= box;
    if (direction === 'UP') snakeY -= box;
    if (direction === 'RIGHT') snakeX += box;
    if (direction === 'DOWN') snakeY += box;

    // Check if snake eats food
    if (snakeX === food.x && snakeY === food.y) {
        food = generateFood();
    } else {
        snake.pop();
    }

    let newHead = {
        x: snakeX,
        y: snakeY
    };

    // Check for collisions with wall or self
    if (snakeX < 0 || snakeY < 0 || snakeX >= canvas.width || snakeY >= canvas.height || collision(newHead, snake)) {
        clearInterval(game);
        gameOver();
    }

    snake.unshift(newHead);
}

// Function to handle game over
function gameOver() {
    gameOverDiv.classList.remove('hidden');
}

// Function to restart the game
function restartGame() {
    snake = [{ x: 10 * box, y: 10 * box }];
    direction = '';
    food = generateFood();
    gameOverDiv.classList.add('hidden');
    game = setInterval(draw, 100);
}

// Start the game
let game = setInterval(draw, 100);
