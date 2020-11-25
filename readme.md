# 2020 임베디드 시스템 및 설계

## Dependencies

```python
pip install pygame pyglm pympler
```

이후 https://pytorch.org/get-started/locally/ 에 접속하여 pytorch 설치

### Windows

https://www.lfd.uci.edu/~gohlke/pythonlibs/ 에 접속하여 pyopengl을 찾은 후 파이썬 버전을 확인하여 (python 3.8이면 cp38 선택) PyOpenGL과 PyOpenGL_accerlate 둘다 설치

### Linux

```
pip install pyopengl pyopengl_accelerate
```

(not tested)

## 실행

```
cd src/raspberry
python main-control.py
```