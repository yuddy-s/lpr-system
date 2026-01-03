# License Plate Recognition (LPR)


<img width="790" height="600" alt="Screenshot 2026-01-02 191130" src="https://github.com/user-attachments/assets/8d36215a-73f8-4b5e-a825-a270c9080193" />
Sample image to be used for recognition

<img width="785" height="596" alt="Screenshot 2026-01-02 191143" src="https://github.com/user-attachments/assets/1ea35e65-bf60-432b-b299-c9bf9fb54e6a" />
Character Recognition Example

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
