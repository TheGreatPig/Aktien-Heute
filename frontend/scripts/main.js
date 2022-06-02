require(['foo'])

function scrollToTop() {
  window.scroll({
    top: 0,
    left: 0,
    behavior: 'smooth'
  });
}

function initCharts(labels, haha) {
    const data = {
      labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul'],
      datasets: [{
        label: 'My First Dataset',
        data: [65, 59, 80, 81, 56, 55, 40],
        fill: false,
        borderColor: '#a3be8c',
      }]
    };
    
    const config = {
        type: 'line',
        data: data,
    };

    const ctx = document.getElementById('myChart');
    const myChart = new Chart(ctx, config)
}

let json = require('./TSLA.json')
console.log(json);