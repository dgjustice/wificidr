# Load library
library(VennDiagram)

# data
arista <- c(
  "tor1.sea",
  "tor2.sea",
  "tor3.sea",
  "tor4.sea",
  "spine1.sea",
  "spine2.sea",
  "tor1.ny",
  "tor2.ny",
  "tor3.ny",
  "tor4.ny",
  "border1.ny",
  "border2.ny",
  "tor1.atl",
  "tor2.atl",
  "tor3.atl",
  "tor4.atl",
  "spine1.atl",
  "spine2.atl"
)
topOfRack <- c(
  "tor1.sea",
  "tor2.sea",
  "tor3.sea",
  "tor4.sea",
  "tor1.ny",
  "tor2.ny",
  "tor3.ny",
  "tor4.ny",
  "tor5.ny",
  "tor6.ny",
  "tor1.atl",
  "tor2.atl",
  "tor3.atl",
  "tor4.atl",
  "tor1.dfw",
  "tor2.dfw"
)
newYork <- c(
  "tor1.ny",
  "tor2.ny",
  "tor3.ny",
  "tor4.ny",
  "tor5.ny",
  "tor6.ny",
  "spine1.ny",
  "spine2.ny",
  "border1.ny",
  "border2.ny"
)

# Chart
VennDiagram::venn.diagram(
  x = list(arista, topOfRack, newYork),
  category.names = c("Arista" , "Top of Rack " , "New York"),
  filename = 'week6_venn.png',
  fill = c("light blue", "pink", "light green"),
  output=TRUE
)

arista