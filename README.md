# License Plate Recognition (LPR)

A simple license plate recognition system using **classical computer vision** and **machine learning**.

**Pipeline:**
- License plate detection via **Connected Component Analysis (CCA)**
- Character segmentation using **region properties**
- Character recognition using a **linear SVM**
- Left-to-right sorting to reconstruct plate text

**Technologies:**
- Python
- NumPy
- scikit-image
- scikit-learn (SVM)
- matplotlib
- joblib

### Running the Program

```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
python prediction.py