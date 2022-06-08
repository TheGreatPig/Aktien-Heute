function scrollToTop() {
  window.scroll({
    top: 0,
    left: 0,
    behavior: 'smooth'
  });
}

async function getRequest(url) {
  const res = await fetch(url);
  const data = await res.json();
  return data
}



async function initChart(symbol, Id) {
  jsonData = await getRequest('http://127.0.0.1:5000/stockdata/' + symbol);
  labels = [];
  datapoints = [];
  for (const x in jsonData['Time Series (5min)']) {
    labels.push(x);
    datapoints.push(jsonData['Time Series (5min)'][x]['4. close']);
  }

  const data = {
    labels: labels,
    datasets: [{
      label: symbol,
      data: datapoints,
      fill: false,
      borderColor: '#a3be8c',
      pointRadius: 1,
    }]
  };
    
  const config = {
      type: 'line',
      data: data,
  };

  const ctx = document.getElementById(symbol);
  const myChart = new Chart(ctx, config)
}

async function initCharts() {
  initChart('TSLA')
  initChart('AMZN')
  initChart('AAPL')
  initChart('AMD')
  initChart('NVDA')
  initChart('MSFT')
  initChart('FB')
}