---
title: "MicroRec: Accelerating Deep Recommendation Systems to Microseconds by Hardware and Data Structure Solutions"
collection: publications
authors_before_me: ~
author_me: "Wenqi Jiang"
authors_after_me: ", Zhenhao He, Shuai Zhang, Thomas B. Preußer, Kai Zeng, Liang Feng, Jiansong Zhang, Tongxuan Liu, Yong Li, Jingren Zhou, Ce Zhang, Gustavo Alonso"
permalink: /publication/2020-10-MicroRec
excerpt: ~
date: 2020-10-17
venue: 'arXiv preprint'
paperurl: ~ 
citation:  ~ 
---

<p></p>

[Paper](https://arxiv.org/pdf/2010.05894.pdf)


Abstract: Deep neural networks are widely used in personalized recommendation systems. Unlike regular DNN inference workloads, recommendation inference is memory-bound due to the many random memory accesses needed to lookup the embedding tables. The inference is also heavily constrained in terms of latency because producing a recommendation for a user must be done in about tens of milliseconds. In this paper, we propose MicroRec, a high-performance inference engine for recommendation systems. MicroRec accelerates recommendation inference by (1) redesigning the data structures involved in the embeddings to reduce the number of lookups needed and (2) taking advantage of the availability of High-Bandwidth Memory (HBM) in FPGA accelerators to tackle the latency by enabling parallel lookups. We have implemented the resulting design on an FPGA board including the embedding lookup step as well as the complete inference process. Compared to the optimized CPU baseline (16 vCPU, AVX2-enabled), MicroRec achieves 13.8∼14.7× speedup on embedding lookup alone and 2.5∼5.4× speedup for the entire recommendation inference in terms of throughput. As for latency, CPU-based engines needs milliseconds for inferring a recommendation while MicroRec only takes microseconds, a significant advantage in real-time recommendation systems.


<!-- Recommended citation: Your Name, You. (2009). "Paper Title Number 1." <i>Journal 1</i>. 1(1). -->