import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Happy Valentine's Day 💕", page_icon="💕", layout="wide")

html_content = '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Happy Valentine's Day 💕</title>
        <style>
            * {
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }

            body {
                background: linear-gradient(135deg, #ffc0cb 0%, #ff69b4 50%, #ff1493 100%);
                min-height: 100vh;
                display: flex;
                align-items: center;
                justify-content: center;
                font-family: 'Arial', sans-serif;
                overflow: hidden;
                position: relative;
            }

            /* Floating hearts background */
            .heart {
                position: fixed;
                width: 20px;
                height: 20px;
                background: #ff1493;
                border-radius: 50% 50% 0 0;
                transform: rotate(-45deg);
                animation: float 6s infinite ease-in;
                opacity: 0.7;
            }

            .heart::before,
            .heart::after {
                content: '';
                position: absolute;
                width: 20px;
                height: 20px;
                background: #ff1493;
                border-radius: 50%;
            }

            .heart::before {
                top: -10px;
                left: 0;
            }

            .heart::after {
                left: 10px;
                top: 0;
            }

            @keyframes float {
                0% {
                    bottom: -50px;
                    opacity: 1;
                }
                100% {
                    bottom: 100vh;
                    opacity: 0;
                    transform: translateX(100px) rotate(-45deg);
                }
            }

            .container {
                text-align: center;
                background: rgba(255, 255, 255, 0.95);
                padding: 60px 40px;
                border-radius: 30px;
                box-shadow: 0 20px 60px rgba(255, 20, 147, 0.4);
                max-width: 600px;
                animation: slideIn 0.8s ease-out;
                z-index: 10;
            }

            @keyframes slideIn {
                from {
                    transform: translateY(50px);
                    opacity: 0;
                }
                to {
                    transform: translateY(0);
                    opacity: 1;
                }
            }

            .title {
                font-size: 3.5em;
                background: linear-gradient(45deg, #ff1493, #ff69b4, #ffc0cb);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                background-clip: text;
                margin-bottom: 20px;
                animation: pulse 2s infinite;
            }

            @keyframes pulse {
                0%, 100% {
                    transform: scale(1);
                }
                50% {
                    transform: scale(1.05);
                }
            }

            .heart-icon {
                font-size: 4em;
                margin: 20px 0;
                animation: heartbeat 1.2s infinite;
                display: inline-block;
            }

            @keyframes heartbeat {
                0%, 100% {
                    transform: scale(1);
                }
                50% {
                    transform: scale(1.2);
                }
            }

            .message {
                font-size: 1.8em;
                color: #ff1493;
                font-weight: bold;
                margin: 25px 0;
                letter-spacing: 1px;
                line-height: 1.6;
            }

            .special-text {
                font-size: 1.4em;
                color: #ff69b4;
                margin: 20px 0;
                font-style: italic;
                line-height: 1.8;
            }

            .buba-text {
                font-size: 2em;
                color: #ff1493;
                font-weight: bold;
                margin: 30px 0;
                text-shadow: 2px 2px 4px rgba(255, 20, 147, 0.3);
                animation: bounce 1s infinite;
            }

            @keyframes bounce {
                0%, 100% {
                    transform: translateY(0);
                }
                50% {
                    transform: translateY(-10px);
                }
            }

            .rose {
                font-size: 2em;
                margin: 20px 10px;
                display: inline-block;
                animation: sway 3s infinite ease-in-out;
            }

            @keyframes sway {
                0%, 100% {
                    transform: rotate(-2deg);
                }
                50% {
                    transform: rotate(2deg);
                }
            }

            .sparkle {
                display: inline-block;
                font-size: 1.5em;
                animation: sparkle 1.5s infinite;
            }

            @keyframes sparkle {
                0%, 100% {
                    opacity: 0.5;
                }
                50% {
                    opacity: 1;
                }
            }

            .separation {
                margin: 30px 0;
                border-bottom: 2px solid #ff1493;
            }

            /* Bear styling */
            .bear {
                font-size: 4em;
                display: inline-block;
                animation: wiggle 2s infinite;
                margin: 20px 0;
            }

            @keyframes wiggle {
                0%, 100% {
                    transform: rotate(0deg);
                }
                25% {
                    transform: rotate(-5deg);
                }
                75% {
                    transform: rotate(5deg);
                }
            }

            /* Butterfly styling */
            .butterfly {
                position: fixed;
                font-size: 2em;
                animation: butterfly-fly 15s infinite ease-in-out;
                z-index: 5;
            }

            @keyframes butterfly-fly {
                0% {
                    top: 80%;
                    left: 0%;
                    transform: rotate(0deg);
                }
                25% {
                    top: 20%;
                    left: 25%;
                    transform: rotate(10deg);
                }
                50% {
                    top: 60%;
                    left: 75%;
                    transform: rotate(-10deg);
                }
                75% {
                    top: 30%;
                    left: 50%;
                    transform: rotate(10deg);
                }
                100% {
                    top: 80%;
                    left: 100%;
                    transform: rotate(0deg);
                }
            }

            /* Star styling */
            .star {
                position: fixed;
                font-size: 1.5em;
                animation: twinkle 2s infinite;
            }

            @keyframes twinkle {
                0%, 100% {
                    opacity: 0.3;
                    transform: scale(0.8);
                }
                50% {
                    opacity: 1;
                    transform: scale(1.2);
                }
            }

            /* Ribbon decoration */
            .ribbon {
                font-size: 2em;
                display: inline-block;
                animation: spin 4s infinite linear;
            }

            @keyframes spin {
                from {
                    transform: rotate(0deg);
                }
                to {
                    transform: rotate(360deg);
                }
            }

            /* Cupid arrow */
            .cupid {
                font-size: 2.5em;
                display: inline-block;
                animation: shoot 3s infinite;
            }

            @keyframes shoot {
                0%, 100% {
                    transform: translateX(0) rotate(45deg);
                }
                50% {
                    transform: translateX(20px) rotate(45deg);
                }
            }

            /* Balloon animation */
            .balloon {
                font-size: 2em;
                display: inline-block;
                animation: balloon-float 3s infinite ease-in-out;
            }

            @keyframes balloon-float {
                0%, 100% {
                    transform: translateY(0px);
                }
                50% {
                    transform: translateY(-15px);
                }
            }

            .button {
                background: linear-gradient(45deg, #ff1493, #ff69b4);
                color: white;
                border: none;
                padding: 15px 40px;
                font-size: 1.2em;
                border-radius: 50px;
                cursor: pointer;
                margin: 15px 10px;
                transition: all 0.3s ease;
                box-shadow: 0 5px 15px rgba(255, 20, 147, 0.3);
                font-weight: bold;
                text-decoration: none;
                display: inline-block;
                user-select: none;
                -webkit-user-select: none;
            }

            .button:hover {
                transform: translateY(-3px);
                box-shadow: 0 8px 20px rgba(255, 20, 147, 0.5);
            }

            .button:active {
                transform: translateY(-1px);
            }

            .spotify-button {
                background: linear-gradient(45deg, #1DB954, #1ed760);
                margin-top: 15px;
            }

            .spotify-button:hover {
                box-shadow: 0 8px 20px rgba(29, 185, 84, 0.5);
            }

            .footer {
                margin-top: 30px;
                font-size: 1.1em;
                color: #ff69b4;
            }

            /* Modal Styles */
            .modal {
                display: none;
                position: fixed;
                z-index: 10000;
                left: 0;
                top: 0;
                width: 100%;
                height: 100%;
                background-color: rgba(0, 0, 0, 0.6);
                animation: fadeIn 0.3s ease-out;
            }

            @keyframes fadeIn {
                from {
                    opacity: 0;
                }
                to {
                    opacity: 1;
                }
            }

            .modal-content {
                background: linear-gradient(135deg, rgba(255, 255, 255, 0.98) 0%, rgba(255, 240, 245, 0.98) 100%);
                margin: 10% auto;
                padding: 40px;
                border-radius: 30px;
                width: 90%;
                max-width: 600px;
                box-shadow: 0 30px 80px rgba(255, 20, 147, 0.4);
                animation: slideInModal 0.5s ease-out;
                border: 3px solid #ff69b4;
            }

            @keyframes slideInModal {
                from {
                    transform: translateY(-50px);
                    opacity: 0;
                }
                to {
                    transform: translateY(0);
                    opacity: 1;
                }
            }

            .close-modal {
                color: #ff1493;
                float: right;
                font-size: 2em;
                font-weight: bold;
                cursor: pointer;
                transition: all 0.3s ease;
            }

            .close-modal:hover {
                transform: scale(1.3) rotate(90deg);
            }

            .modal-title {
                font-size: 2.2em;
                color: #ff1493;
                margin-bottom: 20px;
                text-align: center;
                clear: both;
            }

            .modal-options {
                display: grid;
                grid-template-columns: 1fr;
                gap: 15px;
                margin: 30px 0;
            }

            .option-btn {
                background: linear-gradient(45deg, #ff69b4, #ff1493);
                color: white;
                padding: 18px 25px;
                border: none;
                border-radius: 20px;
                font-size: 1.1em;
                cursor: pointer;
                transition: all 0.3s ease;
                font-weight: bold;
                box-shadow: 0 5px 15px rgba(255, 20, 147, 0.3);
                text-align: left;
                display: flex;
                align-items: center;
                gap: 15px;
            }

            .option-btn:hover {
                transform: translateX(10px) scale(1.02);
                box-shadow: 0 8px 25px rgba(255, 20, 147, 0.5);
            }

            .option-emoji {
                font-size: 1.8em;
            }

            .message-display {
                background: white;
                padding: 25px;
                border-radius: 20px;
                margin: 20px 0;
                border-left: 5px solid #ff69b4;
                font-size: 1.2em;
                color: #ff1493;
                font-weight: bold;
                min-height: 60px;
                display: flex;
                align-items: center;
                justify-content: center;
                text-align: center;
                box-shadow: inset 0 2px 5px rgba(255, 20, 147, 0.1);
            }

            .input-field {
                width: 100%;
                padding: 12px;
                border: 2px solid #ff69b4;
                border-radius: 15px;
                font-size: 1.1em;
                margin: 15px 0;
                box-sizing: border-box;
                font-family: Arial, sans-serif;
            }

            .input-field:focus {
                outline: none;
                border-color: #ff1493;
                box-shadow: 0 0 10px rgba(255, 20, 147, 0.3);
            }
        </style>
    </head>
    <body>
        <!-- Floating hearts -->
        <div class="heart" style="left: 10%; animation-delay: 0s;"></div>
        <div class="heart" style="left: 20%; animation-delay: 1s;"></div>
        <div class="heart" style="left: 30%; animation-delay: 2s;"></div>
        <div class="heart" style="left: 40%; animation-delay: 1.5s;"></div>
        <div class="heart" style="left: 60%; animation-delay: 2.5s;"></div>
        <div class="heart" style="left: 70%; animation-delay: 0.5s;"></div>
        <div class="heart" style="left: 80%; animation-delay: 3s;"></div>
        <div class="heart" style="left: 90%; animation-delay: 1.8s;"></div>

        <!-- Flying butterflies -->
        <div class="butterfly" style="animation-delay: 0s;">🦋</div>
        <div class="butterfly" style="animation-delay: 5s;">🦋</div>
        <div class="butterfly" style="animation-delay: 10s;">🦋</div>

        <!-- Twinkling stars -->
        <div class="star" style="top: 10%; left: 15%;">⭐</div>
        <div class="star" style="top: 20%; left: 85%; animation-delay: 0.5s;">✨</div>
        <div class="star" style="top: 70%; left: 10%; animation-delay: 1s;">⭐</div>
        <div class="star" style="top: 80%; left: 90%; animation-delay: 1.5s;">✨</div>
        <div class="star" style="top: 40%; left: 5%; animation-delay: 0.7s;">⭐</div>
        <div class="star" style="top: 50%; left: 95%; animation-delay: 1.2s;">✨</div>

        <div class="container">
            <div class="heart-icon">💕</div>
            <h1 class="title">Happy Valentine's Day</h1>
            
            <div class="rose">🌹</div>
            <div class="rose">💐</div>
            <div class="rose">🌹</div>

            <div class="message">
                I Love You<br>
                <span class="buba-text">BUBA DUBA!!</span>
            </div>

            <div class="separation"></div>

            <!-- Cute teddy bear -->
            <div class="bear">🧸</div>
            
            <div class="special-text">
                You are the best boyfriend<br>in the world
            </div>

            <div class="separation"></div>

            <div style="margin: 30px 0;">
                <span class="balloon">🎈</span>
                <span class="sparkle">✨</span>
                <span class="rose">💕</span>
                <span class="cupid">💘</span>
                <span class="sparkle">✨</span>
                <span class="balloon">🎈</span>
            </div>

            <div style="margin: 20px 0;">
                <span class="ribbon">🎀</span>
                <span class="rose">💐</span>
                <span class="ribbon">🎀</span>
            </div>

            <div style="margin: 20px 0;">
                <span class="sparkle">💎</span>
                <span class="sparkle">💍</span>
                <span class="sparkle">💎</span>
            </div>

            <div style="margin: 30px 0;">
                <button class="button" onclick="document.getElementById('lovePanel').style.display='block';">Click for Love! 💗</button>
                <br>
                <a href="https://open.spotify.com/track/1WkMMavIMc4JZ8cfMmxHkI?si=6c7d3e8f9a0e4e3d" target="_blank" class="button spotify-button">🎵 Our Summer Song! ☀️</a>
            </div>

            <p class="footer">Forever and always, my love 💕</p>
        </div>

        <!-- Love Message Panel -->
        <div id="lovePanel" style="display: none; position: fixed; bottom: 20px; right: 20px; width: 90%; max-width: 400px; background: white; padding: 25px; border-radius: 20px; border: 3px solid #ff69b4; box-shadow: 0 10px 40px rgba(255, 20, 147, 0.3); z-index: 9999;">
            <div style="text-align: right; margin-bottom: 15px;">
                <span style="cursor: pointer; font-size: 1.8em; color: #ff1493; font-weight: bold;" onclick="document.getElementById('lovePanel').style.display='none';">✕</span>
            </div>
            
            <div style="text-align: center; font-size: 1.8em; color: #ff1493; font-weight: bold; margin-bottom: 20px;">💗 Surprise! 💗</div>
            
            <button style="width: 100%; background: linear-gradient(45deg, #ff1493, #ff69b4); color: white; padding: 12px; border: none; border-radius: 15px; cursor: pointer; margin: 10px 0; font-size: 1.1em; font-weight: bold;" onclick="showRandomMsg(); event.stopPropagation();">🎲 Random Love Message</button>
            
            <button style="width: 100%; background: linear-gradient(45deg, #ff1493, #ff69b4); color: white; padding: 12px; border: none; border-radius: 15px; cursor: pointer; margin: 10px 0; font-size: 1.1em; font-weight: bold;" onclick="doMegaConfetti(); event.stopPropagation();">🎆 Mega Confetti Party!</button>
            
            <div id="msgBox" style="display: none; margin: 15px 0; padding: 15px; background: #fff0f5; border-radius: 15px; font-size: 1.2em; color: #ff1493; font-weight: bold; text-align: center; min-height: 40px;"></div>
        </div>

        <script>
            // Modal Control
            function openLoveModal() {
                document.getElementById('loveModal').style.display = 'block';
                resetModal();
            }

            function closeLoveModal() {
                document.getElementById('loveModal').style.display = 'none';
            }

            function resetModal() {
                document.getElementById('messageDisplay').style.display = 'none';
                document.getElementById('noteInput').style.display = 'none';
                document.getElementById('moodSelector').style.display = 'none';
                document.getElementById('customNote').value = '';
            }

            // Love Messages
            const loveMessages = [
                "You make my heart skip a beat every day! 💓",
                "With you, I found my forever! 🌟",
                "You're not just my love, you're my everything! 💕",
                "Every moment with you is a treasure! 💎",
                "My heart belongs to you completely! 💗",
                "You're the best decision I've ever made! 🎯",
                "Love wasn't in my search history until I found you! 🔍💕",
                "You're my favorite person in the whole universe! 🌌",
                "I fall for you every single day! 😍",
                "With you is my favorite place to be! 🏠💕"
            ];

            function showRandomMsg() {
                try {
                    const randomMsg = loveMessages[Math.floor(Math.random() * loveMessages.length)];
                    const msgBox = document.getElementById('msgBox');
                    msgBox.innerHTML = randomMsg;
                    msgBox.style.display = 'block';
                    createConfetti();
                } catch(e) {
                    console.error('Error:', e);
                }
            }

            function doMegaConfetti() {
                triggerSpecialConfetti();
                document.getElementById('lovePanel').style.display = 'none';
            }

            function triggerSpecialConfetti() {
                // Create LOTS of confetti
                for (let i = 0; i < 50; i++) {
                    const confetti = document.createElement('div');
                    confetti.innerHTML = ['💕', '💖', '💗', '🌹', '✨', '🧸', '🎈', '🦋', '💎', '💍', '🎀', '💘', '⭐'][Math.floor(Math.random() * 13)];
                    confetti.style.position = 'fixed';
                    confetti.style.left = Math.random() * window.innerWidth + 'px';
                    confetti.style.top = '0px';
                    confetti.style.fontSize = (20 + Math.random() * 30) + 'px';
                    confetti.style.zIndex = '9999';
                    confetti.style.pointerEvents = 'none';
                    confetti.style.animation = `float ${3 + Math.random() * 3}s linear forwards`;
                    
                    document.body.appendChild(confetti);
                    
                    setTimeout(() => confetti.remove(), 6000);
                }
            }

            function createConfetti() {
                // Create regular confetti
                for (let i = 0; i < 30; i++) {
                    const confetti = document.createElement('div');
                    confetti.innerHTML = ['💕', '💖', '💗', '🌹', '✨', '🧸', '🎈', '🦋', '💎', '💍', '🎀'][Math.floor(Math.random() * 11)];
                    confetti.style.position = 'fixed';
                    confetti.style.left = Math.random() * window.innerWidth + 'px';
                    confetti.style.top = '0px';
                    confetti.style.fontSize = (20 + Math.random() * 20) + 'px';
                    confetti.style.zIndex = '9999';
                    confetti.style.pointerEvents = 'none';
                    confetti.style.animation = `float ${3 + Math.random() * 2}s linear forwards`;
                    
                    document.body.appendChild(confetti);
                    
                    setTimeout(() => confetti.remove(), 5000);
                }
            }

            // Create initial floating hearts on load
            window.addEventListener('load', () => {
                setInterval(() => {
                    const randomHeart = document.querySelectorAll('.heart');
                    if (randomHeart.length > 0) {
                        randomHeart[Math.floor(Math.random() * randomHeart.length)].style.animation = 'float 6s infinite ease-in';
                    }
                }, 500);
            });
        </script>
    </body>
    </html>
    '''

# Render the HTML content with full height
components.html(html_content, height=1800)
