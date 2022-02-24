Chart.defaults.global = {
    animation: true,
    animationSteps: 60,
    animationEasing: "easeOutIn",
    showScale: true,
    scaleOverride: false,
    scaleSteps: null,
    scaleStepWidth: null,
    scaleStartValue: null,
    scaleLineColor: "#eeeeee",
    scaleLineWidth: 1,
    scaleShowLabels: true,
    scaleLabel: "<%=value%>",
    scaleIntegersOnly: true,
    scaleBeginAtZero: false,
    scaleFontSize: 12,
    scaleFontStyle: "normal",
    scaleFontColor: "#717171",
    responsive: true,
    maintainAspectRatio: true,
    showTooltips: true,
    multiTooltipTemplate: "<%= value %>",
    tooltipFillColor: "#333333",
    tooltipEvents: ["mousemove", "touchstart", "touchmove"],
    tooltipTemplate: "<%if (label){%><%=label%>: <%}%><%= value %>",
    tooltipFontSize: 14,
    tooltipFontStyle: "normal",
    tooltipFontColor: "#fff",
    tooltipTitleFontSize: 16,
    TitleFontStyle : "Raleway",
    tooltipTitleFontStyle: "bold",
    tooltipTitleFontColor: "#ffffff",
    tooltipYPadding: 10,
    tooltipXPadding: 10,
    tooltipCaretSize: 8,
    tooltipCornerRadius: 6,
    tooltipXOffset: 5,
    onAnimationProgress: function(animation) {
        
    },
    onAnimationComplete: function() {}
};



var radarOptions = {
    scaleShowGridLines: true,
    scaleGridLineColor: "rgba(0,0,0,.2)",
    scaleGridLineWidth: 1,
    scaleShowHorizontalLines: true,
    scaleShowVerticalLines: true,
    bezierCurve: true,
    bezierCurveTension: 0.4,
    pointDot: true,
    pointDotRadius: 3,
    pointDotStrokeWidth: 1,
    pointHitDetectionRadius: 20,
    datasetStroke: true,
    datasetStrokeWidth: 2,
    datasetFill: true,
    legendTemplate: "<ul class=\"<%=name.toLowerCase()%>-legend\"><% for (var i=0; i<datasets.length; i++){%><li><span style=\"background-color:<%=datasets[i].strokeColor%>\"></span><%if(datasets[i].label){%><%=datasets[i].label%><%}%></li><%}%></ul>",
    options: {
        animation: {
            tension: {
                duration: 1000,
                easing: 'linear',
                from: 1,
                to: 0,
                loop: true
            }
        },
    }
};
var radarData = {
    labels: ["Ford", "Chevy", "Toyota", "Honda", "Mazda"],
    datasets: [{
        label: "My First dataset",
        fillColor: "rgba(145, 46, 252, 0.4)",
        strokeColor: CubaAdminConfig.primary,
        pointColor: CubaAdminConfig.primary,
        pointStrokeColor: CubaAdminConfig.primary,
        pointHighlightFill: CubaAdminConfig.primary ,
        pointHighlightStroke: "rgba(145, 46, 252, 0.4)",
        data: [12, 3, 5, 18, 7]
    }]
};
       var radarCtx = document.getElementById("myRadarGraph").getContext("2d");
var myRadarChart = new Chart(radarCtx).Radar(radarData, radarOptions);


var polarData = [
    {
        value: 300,
        color: CubaAdminConfig.primary,
        highlight: CubaAdminConfig.primary,
        label: "Yellow"
    }, {
        value: 50,
        color: "#f8d62b",
        highlight: "#f8d62b",
        label: "Sky"
    }, {
        value: 100,
        color: "#51bb25",
        highlight: "#333",
        label: "Black"
    }, {
        value: 40,
        color: "#a927f9",
        highlight: "#a927f9",
        label: "Grey"
    }, {
        value: 120,
        color: CubaAdminConfig.secondary ,
        highlight: CubaAdminConfig.secondary ,
        label: "Dark Grey"
    }
];
var polarOptions = {
    scaleShowLabelBackdrop: true,
    scaleBackdropColor: "rgba(255,255,255,0.75)",
    scaleBeginAtZero: true,
    scaleBackdropPaddingY: 2,
    scaleBackdropPaddingX: 2,
    scaleShowLine: true,
    segmentShowStroke: true,
    segmentStrokeColor: "#fff",
    segmentStrokeWidth: 2,
    animationSteps: 100,
    animationEasing: "easeOutBounce",
    animateRotate: true,
    animateScale: false,
    legendTemplate: "<ul class=\"<%=name.toLowerCase()%>-legend\"><% for (var i=0; i<segments.length; i++){%><li><span style=\"background-color:<%=segments[i].fillColor%>\"></span><%if(segments[i].label){%><%=segments[i].label%><%}%></li><%}%></ul>"
};



var polarCtx = document.getElementById("myPolarGraph").getContext("2d");
var myPolarChart = new Chart(polarCtx).PolarArea(polarData, polarOptions);