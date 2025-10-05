# 标准化与技术创新关系研究项目

## 项目概述

本项目旨在研究标准化（STA）与技术创新投入（TIP）之间的关系，采用联立方程模型（3SLS）分析标准化与技术创新之间的相互影响机制。研究基于面板数据，涵盖多个城市、多个年份的数据。

## 研究框架

### 核心变量
- **TIP** (Technology Innovation Input): 技术创新投入
- **STA** (Standardization): 标准化
- **ECO** (Economic Development): 经济发展水平
- **FDI** (Foreign Direct Investment): 外商直接投资
- **SDC** (Science and Development Capability): 科技发展能力

### 研究方法
- 描述性统计分析
- Pearson相关性分析
- 三阶段最小二乘法（3SLS）联立方程估计
- Hausman检验（固定效应 vs 随机效应）
- 中介效应分析
- 调节效应分析

## 项目结构

```
.
├── data/                          # 数据文件夹
│   ├── data_raw.csv              # 原始数据
│   ├── data.csv                  # 清洗后的数据
│   ├── data_log.csv              # 对数变换数据
│   ├── 量表数据.csv               # 量表数据
│   └── 预调研数据.csv             # 预调研数据
│
├── exports/                       # 导出结果文件夹
│   ├── 中介效应数据.csv
│   ├── 调节效应数据.csv
│   ├── 调节效应斜率图.png
│   ├── 多元线性回归数据.csv
│   └── 量表数据总分.csv
│
├── fonts/                         # 字体文件
│   └── SimHei.ttf                # 黑体字体（用于中文显示）
│
├── analyze.ipynb                  # 主分析notebook
├── dataClean.ipynb               # 数据清洗
├── data_group.ipynb              # 数据分组分析
├── Hausman 检验.ipynb            # Hausman检验
├── model checking.ipynb          # 模型诊断
├── Person.ipynb                  # 个人层面分析
├── Person_pre.ipynb              # 个人层面预处理
└── RStudio.ipynb                 # R语言分析
```

## 环境配置

### 依赖包
```bash
pip install -r requirements.txt
```

主要依赖：
- pandas (~1.3.5)
- numpy
- matplotlib
- seaborn
- scipy
- linearmodels
- scikit-learn
- openpyxl

### 中文显示配置
项目使用SimHei字体支持中文显示，字体文件位于 `fonts/SimHei.ttf`

## 使用说明

### 1. 数据清洗
运行 `dataClean.ipynb` 进行数据预处理和清洗

### 2. 描述性统计分析
运行 `analyze.ipynb` 查看：
- 变量描述性统计
- Pearson相关性分析
- 相关性热力图

### 3. 联立方程模型估计
在 `analyze.ipynb` 中运行3SLS联立方程模型：

**方程1（技术创新投入）：**
```
TIP = β₀ + β₁·STA + β₂·ECO + β₃·FDI + ε₁
```

**方程2（标准化）：**
```
STA = γ₀ + γ₁·TIP + γ₂·ECO + γ₃·SDC + ε₂
```

### 4. 模型检验
- 运行 `Hausman 检验.ipynb` 进行固定效应与随机效应的选择
- 运行 `model checking.ipynb` 进行模型诊断

### 5. 中介/调节效应分析
- 中介效应数据：`exports/中介效应数据.csv`
- 调节效应数据：`exports/调节效应数据.csv`
- 调节效应可视化：`exports/调节效应斜率图.png`

## 主要发现

### 相关性分析
- STA与SDC相关系数最高（r = 0.941, p < 0.001）
- TIP与ECO显著正相关（r = 0.798, p < 0.001）
- TIP与STA显著正相关（r = 0.648, p < 0.001）

### 联立方程结果
**技术创新投入方程（R² = 0.751）：**
- STA系数：62.391 (p = 0.049)，标准化对技术创新投入有显著正向影响
- ECO系数：0.246 (p < 0.001)，经济发展显著促进技术创新投入
- FDI系数：0.047 (p < 0.001)，外商直接投资正向影响技术创新

**标准化方程（R² = 0.891）：**
- TIP系数：-0.0002 (p = 0.118)，技术创新对标准化的影响不显著
- ECO系数：0.0001 (p = 0.003)，经济发展促进标准化
- SDC系数：0.966 (p < 0.001)，科技发展能力对标准化有强烈正向影响

## 数据说明

### 数据来源
- 城市层面面板数据
- 时间跨度：2006-2024
- 包含南京、苏州等多个城市

### 数据文件说明
- `data_raw.csv`: 原始未处理数据
- `data.csv`: 清洗后的标准数据
- `data_log.csv`: 对数变换后的数据（用于消除异方差）
- `量表数据.csv`: 调查问卷量表数据
- `预调研数据.csv`: 预调研阶段收集的数据

## 注意事项

1. 运行notebook前确保已安装所有依赖包
2. 数据文件路径使用相对路径，请保持项目目录结构完整
3. 中文字体显示需要SimHei.ttf字体文件
4. 建议按照以下顺序运行分析：
   - dataClean.ipynb → analyze.ipynb → Hausman 检验.ipynb → model checking.ipynb

## 贡献者

本项目为标准化与技术创新关系的实证研究项目。

## 许可证

本项目仅用于学术研究目的。

---

**最后更新时间**: 2025年10月
