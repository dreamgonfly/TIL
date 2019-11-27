# Cepstrum

A **cepstrum** (/ˈkɛpstrʌm, ˈsɛp-, -strəm/; plural cepstra) is the result of taking the inverse Fourier transform (IFT) of the logarithm of the estimated signal spectrum.

$$\text{power cepstrum of signal} = {\displaystyle =\left|{\mathcal {F}}^{-1}\left\{\log \left(\left|{\mathcal {F}}\{x(t)\}\right|^{2}\right)\right\}\right|^{2}}$$

Many texts define the process as FT → abs() → log → IFT, i.e., that the power cepstrum is the "inverse Fourier transform of the log-magnitude Fourier spectrum". (the difference between squaring or taking the absolute value amounts to an overall factor of 2).

# Meaning

The cepstrum can be seen as information about the rate of change in the different spectrum bands. Cepstrum pitch determination is particularly effective because  are additive in the logarithm of the power spectrum and thus clearly separate. The cepstrum is useful because the low-frequency periodic excitation from the vocal cords (the vocal excitation: pitch) and the formant filtering of the vocal tract (the vocal tract: formants), which convolve in the time domain and multiply in the frequency domain, are additive and in different regions in the quefrency domain.

# The name

The name "cepstrum" was derived by reversing the first four letters of "spectrum". Operations on cepstra are labelled **quefrency analysis** (aka **quefrency alanysis**), **liftering**, or **cepstral analysis**. It may be pronounced in the two ways given, the second having the advantage of avoiding confusion with "kepstrum", which also exists.

# Origin

The power cepstrum was defined in a 1963 paper by Bogert et al. The terms quefrency, alanysis, cepstrum and saphe were invented by the authors by rearranging some letters in frequency, analysis, spectrum and phase. The new invented terms are defined by analogies to the older terms.

# References

[Cepstrum](https://en.wikipedia.org/wiki/Cepstrum)

[Aalto University Wiki](https://wiki.aalto.fi/display/ITSP/Cepstrum+and+MFCC)

[](http://research.cs.tamu.edu/prism/lectures/sp/l9.pdf)