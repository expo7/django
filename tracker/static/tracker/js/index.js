var data = [
  {
    values: [70, 20, 10],

    labels: ["Fat", "Protein", "Carbohydrates"],

    type: "pie",

    textinfo: "label+percent",
    textposition: "inside",
    showlegend: true,
    automargin: true,
  },
];
var layout = {
  title: "Keto Macronutrients",
  autosize: true,

  paper_bgcolor: "#7f7f7f",

  plot_bgcolor: "#c7c7c7",
};

var config = { responsive: true };
try {
  Plotly.newPlot("macroChart", data, layout, config);
} catch (error) {
  console.error(error);
  // expected output: ReferenceError: nonExistentFunction is not defined
  // Note - error messages will vary depending on browser
}

var layout = {
  title: "Fasting Timeline",
  showlegend: true,

  xaxis: {
    title: {
      text: "Time [Hours]",

      font: {
        family: "",

        size: 18,

        color: "#7f7f7f",
      },
    },
  },

  yaxis: {
    title: {
      text: "%",

      font: {
        family: "",

        size: 18,

        color: "#7f7f7f",
      },
    },
  },
  yaxis2: {
    title: "%",

    titlefont: { color: "rgb(148, 103, 189)" },

    tickfont: { color: "rgb(148, 103, 189)" },

    overlaying: "y",

    side: "right",
  },
};

var trace1 = {
  y: [
    100,
    100,
    75,
    75 + 12,
    75,
    75 - 12,
    50,
    80,
    55,
    50,
    50,
    50,
    65,
    50,
    50,
    45,
    40,
    50,
    30,
    25,
    20,
    20,
    20,
    20,
    20,
    20,
  ],

  x: [
    0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90,
    95, 100, 105, 110, 115, 120, 125,
  ],

  type: "scatter",
  name: "Glucose and Insulin",
};

var trace2 = {
  y: [
    0, 0, 0, 0, 0, 12, 12, 20, 23, 25, 35, 40, 55, 55, 55, 55, 60, 65, 70, 75,
    75, 80, 85, 90, 95, 100,
  ],

  x: [
    0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90,
    95, 100, 105, 110, 115, 120, 125,
  ],

  type: "scatter",
  name: "Weight Loss and Keytones",
};

var trace3 = {
  y: [
    0, 0, 0, 0, 0, 0, 30, 35, 40, 45, 50, 55, 60, 70, 70, 70, 75, 80, 80, 85,
    85, 85, 85, 85, 85, 85,
  ],

  x: [
    0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90,
    95, 100, 105, 110, 115, 120, 125,
  ],

  type: "scatter",
  name: "Stem Cells",
};

var trace4 = {
  y: [0],

  x: [72],

  type: "scatter",
  name: "72 Hours",
};

var autophagy = {
  y: [
    0, 0, 0, 10, 15, 20, 20, 30, 40, 50, 60, 70, 80, 90, 100, 95, 85, 80, 70,
    60, 50, 40, 30, 20, 10, 0,
  ],

  x: [
    0, 5, 10, 18, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 72, 75, 80, 85, 90,
    95, 100, 105, 110, 115, 120, 125,
  ],

  type: "scatter",
  name: "Autophagy",
};

var autophagyFill = {
  y: [
    0, 0, 0, 10, 15, 20, 20, 30, 40, 50, 60, 70, 80, 90, 100, 95, 85, 80, 70,
    80, 90, 100,
  ],

  x: [0, 5, 10, 18, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 72],

  type: "scatter",
  fill: "tozeroy",
  name: "Increasing Hgh",
};

var autophagyFill2 = {
  y: [100, 95, 85, 80, 70, 60, 50, 40, 30, 20, 10, 0],

  x: [72, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125],

  type: "scatter",
  fill: "tozeroy",
  name: "Declineing Hgh",
};
var seventyTwo = {
  x: [72, 72],

  y: [100, 0],

  mode: "text+lines",

  type: "scatter",

  name: "Peak Muscle Protection",

  text: ["Peak Muscle Protection 72 Hours"],

  textfont: {
    family: "Times New Roman",
  },

  textposition: "top center",

  marker: { size: 12 },
};

var eightTeen = {
  x: [18],

  y: [0],

  mode: "text+markers",

  type: "scatter",

  name: "Ketone Production Begins",

  text: ["Ketone production starts 12 Hours"],

  textfont: {
    family: "Times New Roman",
  },

  textposition: "bottom center",

  marker: { size: 18 },
};





var ketone = {
  x: [0, 12, 20],

  y: [0, 0, 100],

  type: "scatter",

  name: "Ketones",

  mode: "markers",

  marker: { size: 18 },
  line: {
    dash: "dot",
    color: "green",

    width: 4,
  },

  text: ["Ketones"],
  fill: "tozeroy",

};

var config = { responsive: true };
var layout = {
  title: "Ketones",

  showlegend: false,
xaxis:{
   title: {
      text: "Hours",

      font: {
        family: "",

        size: 18,

        color: "#7f7f7f",
      },
    },
  },

  yaxis: {
    title: {
      text: "%",

      font: {
        family: "",

        size: 18,

        color: "#7f7f7f",
      },
    },
  },
};


var ketone_text= {
  x: [12,18],

  y: [10,100],

  mode: "text",

  type: "scatter",

  name: "Ketone Production Begins",

  text: ["Ketone production starts 12 Hours","6+ hours in ketois"],

  textfont: {
    family: "Times New Roman",
  },

  textposition: "top center",

  marker: { size: 18 },
};

try {
  Plotly.newPlot("keytoneChart", [ketone,ketone_text],layout,config);
} catch (error) {
  console.error(error);
  // expected output: ReferenceError: nonExistentFunction is not defined
  // Note - error messages will vary depending on browser
}
