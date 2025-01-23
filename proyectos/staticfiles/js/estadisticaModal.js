document.addEventListener('DOMContentLoaded', function () {
    // Escuchar el evento de apertura del modal usando jQuery
    $('#modalEstadisticas').on('shown.bs.modal', function () {
        fetch('/queries/estadisticas/') // Cambia esta URL si es necesario
            .then(response => response.json())
            .then(data => {
                // Obtener el contexto del lienzo
                const ctx = document.getElementById('graficaEstadistica').getContext('2d');

                // Limpiar cualquier gráfico previo
                if (window.myChart) {
                    window.myChart.destroy();
                }

                // Crear el gráfico
                window.myChart = new Chart(ctx, {
                    type: 'line',// Cambia a 'line', 'pie', 'bar', 'doughnut', 'polarArea','radar', 
                    data: {
                        labels: data.labels,
                        datasets: data.datasets
                    },
                    options: {
                        responsive: true,
                        scales: {
                            y: {
                                beginAtZero: true
                            }
                        }
                    }
                });
            })
            .catch(error => {
                console.error('Error al obtener las estadísticas:', error);
                Swal.fire('Error', 'No se pudieron cargar las estadísticas.', 'error');
            });
    });
});
