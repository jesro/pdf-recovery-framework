let currentPlan = null;

async function loadProfiles() {
    const select = document.getElementById("profile-select");
    select.innerHTML = "";

    const response = await fetch("/profiles");
    const profiles = await response.json();

    for (const name in profiles) {
        const option = document.createElement("option");
        option.value = name;
        option.text = name;
        select.appendChild(option);
    }
}

async function uploadPDF() {
    const fileInput = document.getElementById("pdf-file");
    if (!fileInput.files.length) return alert("Select a PDF file");

    const formData = new FormData();
    formData.append("file", fileInput.files[0]);

    const response = await fetch("/upload", { method: "POST", body: formData });
    const result = await response.json();

    document.getElementById("file-info").innerText = 
        `Uploaded: ${result.filename} | Size: ${result.size_kb} KB | SHA256: ${result.hash}`;
}

async function buildPlan() {
    const profile = document.getElementById("profile-select").value;
    const response = await fetch("/plan", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ profile })
    });
    currentPlan = await response.json();
    document.getElementById("plan-preview").innerText = JSON.stringify(currentPlan, null, 2);
    simulateProgress();
}

function exportPlan() {
    if (!currentPlan) return alert("Build a plan first");
    const blob = new Blob([JSON.stringify(currentPlan, null, 2)], { type: "application/json" });
    const url = URL.createObjectURL(blob);
    const a = document.createElement("a");
    a.href = url;
    a.download = "plan.json";
    a.click();
}

function simulateProgress() {
    const progress = document.getElementById("progress-bar");
    progress.value = 0;
    const interval = setInterval(() => {
        if (progress.value >= 100) clearInterval(interval);
        else progress.value += 1;
    }, 50); // 5 seconds simulation
}

window.onload = loadProfiles;