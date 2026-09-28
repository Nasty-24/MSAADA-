const API_URL = "http://127.0.0.1:8000";
const APP_NAME = "msaada";
const USER_ID = "citizen";

const chat = document.getElementById("chat");
const form = document.getElementById("chat-form");
const messageInput = document.getElementById("message");
const sendButton = document.getElementById("send-btn");
const status = document.getElementById("status");
const errorBox = document.getElementById("error");

let sessionId = null;
let sending = false;


/* =========================
   CHAT UI
========================= */

function addMessage(text, sender) {
    const message = document.createElement("div");
    message.className = `message ${sender}`;

    const avatar = document.createElement("div");
    avatar.className = "avatar";
    avatar.textContent = sender === "user" ? "You" : "M";

    const bubble = document.createElement("div");
    bubble.className = "bubble";
    bubble.innerHTML = formatResponse(text);

    message.appendChild(avatar);
    message.appendChild(bubble);

    chat.appendChild(message);
    chat.scrollTop = chat.scrollHeight;
}


function formatResponse(text) {
    if (!text) return "";

    let html = escapeHtml(text);

    html = html.replace(
        /\[([^\]]+)\]\((https?:\/\/[^\s)]+)\)/g,
        '<a href="$2" target="_blank" rel="noopener noreferrer">$1</a>'
    );

    html = html.replace(/\*\*(.*?)\*\*/g, "<strong>$1</strong>");

    html = html.replace(/^### (.*)$/gm, "<strong>$1</strong>");

    html = html.replace(/^## (.*)$/gm, "<strong>$1</strong>");

    html = html.replace(/^- (.*)$/gm, "• $1");

    html = html.replace(/\n/g, "<br>");

    return html;
}


function escapeHtml(text) {
    const div = document.createElement("div");
    div.textContent = text;
    return div.innerHTML;
}


/* =========================
   STATUS
========================= */

async function checkConnection() {
    try {
        const response = await fetch(`${API_URL}/list-apps`);

        if (!response.ok) {
            throw new Error(`HTTP ${response.status}`);
        }

        const apps = await response.json();

        if (!apps.includes(APP_NAME)) {
            throw new Error("MSAADA app not found");
        }

        status.innerHTML =
            '<span class="status-dot online"></span> MSAADA Online';

        status.classList.add("online");

        return true;

    } catch (error) {

        console.error("Connection check:", error);

        status.innerHTML =
            '<span class="status-dot offline"></span> Connection problem';

        status.classList.add("offline");

        return false;
    }
}


/* =========================
   SESSION
========================= */

async function createSession() {

    sessionId =
        "session-" +
        Date.now() +
        "-" +
        Math.random().toString(36).substring(2, 8);

    const url =
        `${API_URL}/apps/${APP_NAME}/users/${USER_ID}/sessions/${sessionId}`;

    console.log("Creating session:", url);

    const response = await fetch(url, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({})
    });

    if (!response.ok) {

        const text = await response.text();

        throw new Error(
            `Session creation failed: ${response.status} ${text}`
        );
    }

    console.log("Session created:", sessionId);

    return sessionId;
}


/* =========================
   SEND MESSAGE
========================= */

async function sendMessage(text) {

    if (sending) {
        return;
    }

    const cleanText = text.trim();

    if (!cleanText) {
        return;
    }

    sending = true;

    clearError();

    addMessage(cleanText, "user");

    messageInput.value = "";

    sendButton.disabled = true;
    sendButton.textContent = "Thinking...";

    try {

        /* Make sure a valid ADK session exists */
        if (!sessionId) {
            await createSession();
        }


        const payload = {
            app_name: APP_NAME,
            user_id: USER_ID,
            session_id: sessionId,

            new_message: {
                role: "user",
                parts: [
                    {
                        text: cleanText
                    }
                ]
            }
        };

        console.log("Sending to ADK:", payload);


        const response = await fetch(`${API_URL}/run`, {
            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify(payload)
        });


        if (!response.ok) {

            const errorText = await response.text();

            console.error(
                "ADK /run error:",
                response.status,
                errorText
            );

            throw new Error(
                `ADK returned ${response.status}: ${errorText}`
            );
        }


        const data = await response.json();

        console.log("ADK response:", data);


        const answer = extractResponse(data);


        if (!answer) {
            throw new Error("ADK returned no text response.");
        }


        addMessage(answer, "assistant");


    } catch (error) {

        console.error("MSAADA request failed:", error);

        showError(
            "MSAADA could not complete the request. " +
            "Please check the ADK server."
        );

    } finally {

        sending = false;

        sendButton.disabled = false;
        sendButton.textContent = "Send";

        messageInput.focus();
    }
}


/* =========================
   EXTRACT ADK RESPONSE
========================= */

function extractResponse(data) {

    if (Array.isArray(data)) {

        for (let i = data.length - 1; i >= 0; i--) {

            const event = data[i];

            if (
                event &&
                event.content &&
                Array.isArray(event.content.parts)
            ) {

                const texts = event.content.parts
                    .filter(part => part.text)
                    .map(part => part.text);

                if (texts.length > 0) {
                    return texts.join("\n");
                }
            }
        }
    }


    if (data && data.text) {
        return data.text;
    }


    if (
        data &&
        data.content &&
        Array.isArray(data.content.parts)
    ) {

        return data.content.parts
            .filter(part => part.text)
            .map(part => part.text)
            .join("\n");
    }


    return "";
}


/* =========================
   SUGGESTION BUTTONS
========================= */

function useSuggestion(text) {

    if (sending) {
        return;
    }

    messageInput.value = text;

    /*
       Do NOT use requestSubmit here.
       Directly send the message once.
    */
    sendMessage(text);
}


/* =========================
   FORM
========================= */

form.addEventListener("submit", function(event) {

    event.preventDefault();

    if (sending) {
        return;
    }

    sendMessage(messageInput.value);
});


messageInput.addEventListener("keydown", function(event) {

    if (event.key === "Enter") {

        event.preventDefault();

        if (!sending) {
            form.requestSubmit();
        }
    }
});


/* =========================
   ERRORS
========================= */

function showError(message) {

    errorBox.textContent = message;
    errorBox.style.display = "block";
}


function clearError() {

    errorBox.textContent = "";
    errorBox.style.display = "none";
}


/* =========================
   STARTUP
========================= */

checkConnection();