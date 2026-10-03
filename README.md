# Traxis HEP Capstone

This repository contains Traxis 1.0.2, a Python and PyQt desktop application
for analysing particle tracks in digitized bubble-chamber images. The toolkit
supports track-momentum calculations, optical-density measurements, angular
measurements, saved analysis sessions and annotated screenshots.

The application source and its user, calibration and film-digitization guides
are located in [`traxis-1.0.2/`](traxis-1.0.2/).

## Authors

The bundled project documentation credits Syed Haider Abidi, Nooruddin Ahmed,
Christopher Dydula, Anas Ali and Ruchir Tullu.

## Setup

Python 3.8 or newer is recommended for the current PyQt5 packages.

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
python -m pip install -r requirements.txt
```

## Run

From the repository root:

```bash
cd traxis-1.0.2
python runtraxis
```

Consult `traxis_User_Guide Updated.docx`, `Calibration_Guide.doc` and
`Film_Digitization_Guide.doc` before analysing an image.

## Repository hygiene

Generated Python bytecode, operating-system metadata and local JSON session
files are excluded from version control.

## Tests and continuous integration

The automated tests verify the numerical circle-fitting calculation using
synthetic points with a known centre and radius:

```bash
python -m unittest discover -s tests -v
```

GitHub Actions compiles the source and runs these headless numerical tests on
Python 3.11 for every push and pull request. Full GUI interaction remains a
manual test because it requires an interactive desktop and image input.

## Licence

Traxis is distributed under the GNU General Public License v3.0. See
[`traxis-1.0.2/LICENSE`](traxis-1.0.2/LICENSE).
