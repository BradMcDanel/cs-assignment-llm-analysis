import subprocess
import os

def run_main_py(input_file):
   return subprocess.check_output(["python", "main.py", input_file], universal_newlines=True)

def read_output_file(output_file):
   with open(output_file, "r") as file:
       return file.read().strip()

def predators_and_prey(input_file, output_file):
   main_output = run_main_py(input_file)
   expected_output = read_output_file(output_file)

   main_lines = main_output.split("\n")
   expected_lines = expected_output.split("\n")

   for line in expected_lines:
       if line.startswith(tuple(f"{predator} eats" for predator in expected_lines if "eats" in predator)):
           assert any(subline.strip() == line.strip() for subline in main_lines)

def apex_predators(input_file, output_file):
   main_output = run_main_py(input_file)
   expected_output = read_output_file(output_file)

   main_lines = main_output.split("\n")
   expected_lines = expected_output.split("\n")

   apex_predators_line = next((line for line in expected_lines if line.startswith("Apex Predators:")), None)
   assert any(subline.strip() == apex_predators_line.strip() for subline in main_lines if subline.startswith("Apex Predators:"))

def producers(input_file, output_file):
   main_output = run_main_py(input_file)
   expected_output = read_output_file(output_file)

   main_lines = main_output.split("\n")
   expected_lines = expected_output.split("\n")

   producers_line = next((line for line in expected_lines if line.startswith("Producers:")), None)
   assert any(subline.strip() == producers_line.strip() for subline in main_lines if subline.startswith("Producers:"))

def most_flexible_eaters(input_file, output_file):
   main_output = run_main_py(input_file)
   expected_output = read_output_file(output_file)

   main_lines = main_output.split("\n")
   expected_lines = expected_output.split("\n")

   most_flexible_eaters_line = next((line for line in expected_lines if line.startswith("Most Flexible Eaters:")), None)
   assert any(subline.strip() == most_flexible_eaters_line.strip() for subline in main_lines if subline.startswith("Most Flexible Eaters:"))

def tastiest(input_file, output_file):
   main_output = run_main_py(input_file)
   expected_output = read_output_file(output_file)

   main_lines = main_output.split("\n")
   expected_lines = expected_output.split("\n")

   tastiest_line = next((line for line in expected_lines if line.startswith("Tastiest:")), None)
   assert any(subline.strip() == tastiest_line.strip() for subline in main_lines if subline.startswith("Tastiest:"))

def heights(input_file, output_file):
   main_output = run_main_py(input_file)
   expected_output = read_output_file(output_file)

   main_lines = main_output.split("\n")
   expected_lines = expected_output.split("\n")

   heights_lines = [line for line in expected_lines if ":" in line and line.split(":")[1].strip().isdigit()]
   for line in heights_lines:
       assert any(subline.strip() == line.strip() for subline in main_lines)

def herbivores(input_file, output_file):
   main_output = run_main_py(input_file)
   expected_output = read_output_file(output_file)

   main_lines = main_output.split("\n")
   expected_lines = expected_output.split("\n")

   herbivores_line = next((line for line in expected_lines if line.startswith("Herbivores:")), None)
   assert any(subline.strip() == herbivores_line.strip() for subline in main_lines if subline.startswith("Herbivores:"))

def omnivores(input_file, output_file):
   main_output = run_main_py(input_file)
   expected_output = read_output_file(output_file)

   main_lines = main_output.split("\n")
   expected_lines = expected_output.split("\n")

   omnivores_line = next((line for line in expected_lines if line.startswith("Omnivores:")), None)
   assert any(subline.strip() == omnivores_line.strip() for subline in main_lines if subline.startswith("Omnivores:"))

def carnivores(input_file, output_file):
   main_output = run_main_py(input_file)
   expected_output = read_output_file(output_file)

   main_lines = main_output.split("\n")
   expected_lines = expected_output.split("\n")

   carnivores_line = next((line for line in expected_lines if line.startswith("Carnivores:")), None)
   assert any(subline.strip() == carnivores_line.strip() for subline in main_lines if subline.startswith("Carnivores:"))

def test_another_predators_and_prey():
    input_file = "AnotherFoodWeb.txt"
    output_file = "AnotherFoodWeb_Output.txt"
    predators_and_prey(input_file, output_file)

def test_another_apex_predators():
    input_file = "AnotherFoodWeb.txt"
    output_file = "AnotherFoodWeb_Output.txt"
    apex_predators(input_file, output_file)

def test_another_producers():
    input_file = "AnotherFoodWeb.txt"
    output_file = "AnotherFoodWeb_Output.txt"
    producers(input_file, output_file)

def test_another_most_flexible_eaters():
    input_file = "AnotherFoodWeb.txt"
    output_file = "AnotherFoodWeb_Output.txt"
    most_flexible_eaters(input_file, output_file)

def test_another_tastiest():
    input_file = "AnotherFoodWeb.txt"
    output_file = "AnotherFoodWeb_Output.txt"
    tastiest(input_file, output_file)

def test_another_heights():
    input_file = "AnotherFoodWeb.txt"
    output_file = "AnotherFoodWeb_Output.txt"
    heights(input_file, output_file)

def test_another_herbivores():
    input_file = "AnotherFoodWeb.txt"
    output_file = "AnotherFoodWeb_Output.txt"
    herbivores(input_file, output_file)

def test_another_omnivores():
    input_file = "AnotherFoodWeb.txt"
    output_file = "AnotherFoodWeb_Output.txt"
    omnivores(input_file, output_file)

def test_another_carnivores():
    input_file = "AnotherFoodWeb.txt"
    output_file = "AnotherFoodWeb_Output.txt"
    carnivores(input_file, output_file)

def test_aquatic_predators_and_prey():
    input_file = "AquaticFoodWeb.txt"
    output_file = "AquaticFoodWeb_Output.txt"
    predators_and_prey(input_file, output_file)

def test_aquatic_apex_predators():
    input_file = "AquaticFoodWeb.txt"
    output_file = "AquaticFoodWeb_Output.txt"
    apex_predators(input_file, output_file)

def test_aquatic_producers():
    input_file = "AquaticFoodWeb.txt"
    output_file = "AquaticFoodWeb_Output.txt"
    producers(input_file, output_file)

def test_aquatic_most_flexible_eaters():
    input_file = "AquaticFoodWeb.txt"
    output_file = "AquaticFoodWeb_Output.txt"
    most_flexible_eaters(input_file, output_file)

def test_aquatic_tastiest():
    input_file = "AquaticFoodWeb.txt"
    output_file = "AquaticFoodWeb_Output.txt"
    tastiest(input_file, output_file)

def test_aquatic_heights():
    input_file = "AquaticFoodWeb.txt"
    output_file = "AquaticFoodWeb_Output.txt"
    heights(input_file, output_file)

def test_aquatic_herbivores():
    input_file = "AquaticFoodWeb.txt"
    output_file = "AquaticFoodWeb_Output.txt"
    herbivores(input_file, output_file)

def test_aquatic_omnivores():
    input_file = "AquaticFoodWeb.txt"
    output_file = "AquaticFoodWeb_Output.txt"
    omnivores(input_file, output_file)

def test_aquatic_carnivores():
    input_file = "AquaticFoodWeb.txt"
    output_file = "AquaticFoodWeb_Output.txt"
    carnivores(input_file, output_file)

def test_grassland_predators_and_prey():
    input_file = "GrasslandFoodWeb.txt"
    output_file = "GrasslandFoodWeb_Output.txt"
    predators_and_prey(input_file, output_file)

def test_grassland_apex_predators():
    input_file = "GrasslandFoodWeb.txt"
    output_file = "GrasslandFoodWeb_Output.txt"
    apex_predators(input_file, output_file)

def test_grassland_producers():
    input_file = "GrasslandFoodWeb.txt"
    output_file = "GrasslandFoodWeb_Output.txt"
    producers(input_file, output_file)

def test_grassland_most_flexible_eaters():
    input_file = "GrasslandFoodWeb.txt"
    output_file = "GrasslandFoodWeb_Output.txt"
    most_flexible_eaters(input_file, output_file)

def test_grassland_tastiest():
    input_file = "GrasslandFoodWeb.txt"
    output_file = "GrasslandFoodWeb_Output.txt"
    tastiest(input_file, output_file)

def test_grassland_heights():
    input_file = "GrasslandFoodWeb.txt"
    output_file = "GrasslandFoodWeb_Output.txt"
    heights(input_file, output_file)

def test_grassland_herbivores():
    input_file = "GrasslandFoodWeb.txt"
    output_file = "GrasslandFoodWeb_Output.txt"
    herbivores(input_file, output_file)

def test_grassland_omnivores():
    input_file = "GrasslandFoodWeb.txt"
    output_file = "GrasslandFoodWeb_Output.txt"
    omnivores(input_file, output_file)

def test_grassland_carnivores():
    input_file = "GrasslandFoodWeb.txt"
    output_file = "GrasslandFoodWeb_Output.txt"
    carnivores(input_file, output_file)

def test_mixed_predators_and_prey():
    input_file = "MixedFoodWeb.txt"
    output_file = "MixedFoodWeb_Output.txt"
    predators_and_prey(input_file, output_file)

def test_mixed_apex_predators():
    input_file = "MixedFoodWeb.txt"
    output_file = "MixedFoodWeb_Output.txt"
    apex_predators(input_file, output_file)

def test_mixed_producers():
    input_file = "MixedFoodWeb.txt"
    output_file = "MixedFoodWeb_Output.txt"
    producers(input_file, output_file)

def test_mixed_most_flexible_eaters():
    input_file = "MixedFoodWeb.txt"
    output_file = "MixedFoodWeb_Output.txt"
    most_flexible_eaters(input_file, output_file)

def test_mixed_tastiest():
    input_file = "MixedFoodWeb.txt"
    output_file = "MixedFoodWeb_Output.txt"
    tastiest(input_file, output_file)

def test_mixed_heights():
    input_file = "MixedFoodWeb.txt"
    output_file = "MixedFoodWeb_Output.txt"
    heights(input_file, output_file)

def test_mixed_herbivores():
    input_file = "MixedFoodWeb.txt"
    output_file = "MixedFoodWeb_Output.txt"
    herbivores(input_file, output_file)

def test_mixed_omnivores():
    input_file = "MixedFoodWeb.txt"
    output_file = "MixedFoodWeb_Output.txt"
    omnivores(input_file, output_file)

def test_mixed_carnivores():
    input_file = "MixedFoodWeb.txt"
    output_file = "MixedFoodWeb_Output.txt"
    carnivores(input_file, output_file)

def test_simple_predators_and_prey():
    input_file = "SimpleFoodWeb.txt"
    output_file = "SimpleFoodWeb_Output.txt"
    predators_and_prey(input_file, output_file)

def test_simple_apex_predators():
    input_file = "SimpleFoodWeb.txt"
    output_file = "SimpleFoodWeb_Output.txt"
    apex_predators(input_file, output_file)

def test_simple_producers():
    input_file = "SimpleFoodWeb.txt"
    output_file = "SimpleFoodWeb_Output.txt"
    producers(input_file, output_file)

def test_simple_most_flexible_eaters():
    input_file = "SimpleFoodWeb.txt"
    output_file = "SimpleFoodWeb_Output.txt"
    most_flexible_eaters(input_file, output_file)

def test_simple_tastiest():
    input_file = "SimpleFoodWeb.txt"
    output_file = "SimpleFoodWeb_Output.txt"
    tastiest(input_file, output_file)

def test_simple_heights():
    input_file = "SimpleFoodWeb.txt"
    output_file = "SimpleFoodWeb_Output.txt"
    heights(input_file, output_file)

def test_simple_herbivores():
    input_file = "SimpleFoodWeb.txt"
    output_file = "SimpleFoodWeb_Output.txt"
    herbivores(input_file, output_file)

def test_simple_omnivores():
    input_file = "SimpleFoodWeb.txt"
    output_file = "SimpleFoodWeb_Output.txt"
    omnivores(input_file, output_file)

def test_simple_carnivores():
    input_file = "SimpleFoodWeb.txt"
    output_file = "SimpleFoodWeb_Output.txt"
    carnivores(input_file, output_file)

def test_terrestrial_predators_and_prey():
    input_file = "TerrestrialFoodWeb.txt"
    output_file = "TerrestrialFoodWeb_Output.txt"
    predators_and_prey(input_file, output_file)

def test_terrestrial_apex_predators():
    input_file = "TerrestrialFoodWeb.txt"
    output_file = "TerrestrialFoodWeb_Output.txt"
    apex_predators(input_file, output_file)

def test_terrestrial_producers():
    input_file = "TerrestrialFoodWeb.txt"
    output_file = "TerrestrialFoodWeb_Output.txt"
    producers(input_file, output_file)

def test_terrestrial_most_flexible_eaters():
    input_file = "TerrestrialFoodWeb.txt"
    output_file = "TerrestrialFoodWeb_Output.txt"
    most_flexible_eaters(input_file, output_file)

def test_terrestrial_tastiest():
    input_file = "TerrestrialFoodWeb.txt"
    output_file = "TerrestrialFoodWeb_Output.txt"
    tastiest(input_file, output_file)

def test_terrestrial_heights():
    input_file = "TerrestrialFoodWeb.txt"
    output_file = "TerrestrialFoodWeb_Output.txt"
    heights(input_file, output_file)

def test_terrestrial_herbivores():
    input_file = "TerrestrialFoodWeb.txt"
    output_file = "TerrestrialFoodWeb_Output.txt"
    herbivores(input_file, output_file)

def test_terrestrial_omnivores():
    input_file = "TerrestrialFoodWeb.txt"
    output_file = "TerrestrialFoodWeb_Output.txt"
    omnivores(input_file, output_file)

def test_terrestrial_carnivores():
    input_file = "TerrestrialFoodWeb.txt"
    output_file = "TerrestrialFoodWeb_Output.txt"
    carnivores(input_file, output_file)
