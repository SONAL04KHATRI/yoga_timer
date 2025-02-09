function startTimer() {
    let minutes = document.getElementById("minutes").value;
    fetch('/start', {
        method: 'POST',
        body: JSON.stringify({ minutes: minutes }),
        headers: { 'Content-Type': 'application/json' }
    }).then(response => response.json())
      .then(data => updateTimer());
}

function pauseTimer() {
    fetch('/pause', { method: 'POST' })
      .then(response => response.json())
      .then(data => updateTimer());
}

function resetTimer() {
    fetch('/reset', { method: 'POST' })
      .then(response => response.json())
      .then(data => document.getElementById("time-left").innerText = 0);
}

function updateTimer() {
    setInterval(() => {
        fetch('/start')
          .then(response => response.json())
          .then(data => document.getElementById("time-left").innerText = data.time_left);
    }, 1000);
}
