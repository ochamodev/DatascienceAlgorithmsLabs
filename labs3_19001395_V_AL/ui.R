library(shiny)
library(shinydashboard)

# Problem 1
closedSolutionMenuTitle <- "P1 Solución cerrada"
closedSolutionMenuId <- "closed_solution"
closedSolutionResolveBtn <- "Solve closed solution"
closedSolutionResolveBtn <- "closedSolutionResolve"
# Problem 1

# Define UI for application that draws a histogram
dashboardPage(
    dashboardHeader(title = "Algoritmos en la Ciencia de Datos"),
    dashboardSidebar(
        sidebarMenu(
            menuItem(closedSolutionMenuTitle, tabName = closedSolutionMenuId),
            menuItem("Derivación", tabName = "Derivacion")
        )
    ),
    dashboardBody(
        tabItems(
            tabItem(closedSolutionMenuTitle,
                    h1(closedSolutionMenuTitle),
                    box(textInput("ecuacion", "Ingrese la Ecuación"),
                        textInput("initVal", "X0"),
                        textInput("Error", "Error")),
                    actionButton(close, closedSolutionMenuTitle),
                    tableOutput("salidaTabla")),
            
            tabItem("Derivacion",
                    h1("Diferencias Finitas"),
                    box(textInput("difFinEcu", "Ingrese la Ecuación"),
                    textInput("valorX", "x"),
                    textInput("valorH", "h")),
                    actionButton("diferFinEval", "Evaluar Derivada"),
                    textOutput("difFinitOut"))
        )
    )
)
