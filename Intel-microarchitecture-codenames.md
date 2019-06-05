# Intel microarchitecture codenames

Skylake, Kaby Lake, Coffee Lake, Cannon Lake, Whiskey Lake, Coffee Lake Refresh, Ice Lake are the codenames for Intel processor microarchitectures. It's worth pointing out that Intel is currently on it's fifth generation of mainstream 14nm products (Broadwell, Skylake, Kaby Lake, Coffee Lake, and CFL-R).

# Skylake (SKL, 14nm, 6th Gen Core, August 2015)

The first of the "Lake" CPUs, Skylake was a major CPU architecture overhaul. Intel moved from a 4-wide design to a **6-wide design** (meaning, **fetch, decode, and execute up to six instructions per clock cycle**). It was the **second of Intel's 14nm CPUs**—the **"tock" to Broadwell's "tick,"** though of course Intel abandoned Tick-Tock shortly after. Desktop and mobile variants were either 2-core or 4-core, with and without **Hyper-Threading (aka SMT, Symmetric Multi-Threading)** depending on the family. Skylake also served as the introduction for Intel's **Gen9 graphics** technology, with improved performance and features. Skylake CPUs share its microarchitecture with Kaby Lake, Coffee Lake and Cannon Lake CPUs.

Intel officially end of life and discontinued Skylake LGA 1151 CPUs on March 4, 2019.

# Kaby Lake (KBL, 14nm+, 7th Gen Core, August 2016)

Kaby Lake represented the official end of Tick-Tock. Fundamentally, Kaby Lake is the same architecture as Skylake, but the **manufacturing process was refined**—hence the "+" on 14nm+. The changes consist of a modified fin profile and strained silicon, plus refinements in manufacturing that naturally occur as a process matures.

Desktop and mobile variants were the same 2-core and 4-core designs as SKL, and for the first time Pentium brand CPUs enabled Hyper-Threading (I'm not counting the original Pentium 4 Hyper-Threading). Kaby Lake also updated the graphics core to **Gen9.5**, the major changes involving support for 4K HEVC/VP9 video decoding.

# Coffee Lake (CFL, 14nm++, 8th Gen Core, October 2017)

Coffee Lake wasn't on Intel's original roadmaps—it was likely introduced to counter **AMD's Zen architecture**, which promised up to 8-core/16-thread designs at mainstream prices. Coffee Lake also spelled the end of Intel's "Process-Architecture-Optimization" plans, since it represented a **second optimization phase**. CFL keeps the **Gen9.5** graphics.

14nm++ increased the transistor gate pitch for lower current density and higher leakage transistors. That in turn allows for higher frequencies, though with larger die sizes and increased idle power use. The biggest change was mainstream desktop 6-core/12-thread designs for Core i7, 6-core/6-thread for Core i5, and 4-core/4-thread for Core i3. Mobile models also got 6-core 45W CPUs for the first time.

# Cannon Lake (CNL, 10nm, 8th Gen Core, May 2018)

The ephemeral Cannon Lake, Intel's first 10nm processor design.

Originally intended to launch in 2016, first demonstrated in 2017, and first shipped in *very* limited quantities in May 2018, Cannon Lake had more than a few issues. [Intel's Cannon Lake page](https://ark.intel.com/content/www/us/en/ark/products/codename/48994/cannon-lake.html) (which is linked from the [Core i3-8121U](https://ark.intel.com/content/www/us/en/ark/products/136863/intel-core-i3-8121u-processor-4m-cache-up-to-3-20-ghz.html), the only Cannon Lake CPU as far as we're aware), doesn't even exist.

How bad was Intel's first stab at 10nm? Cannon Lake does include **AVX512 instruction** support, which can help in a few specific instances, but everything else is basically bad. Power, memory latency, and other elements were worse than with existing 14nm mobile designs. In retrospect, the difficulties caused by all the enhancements originally stuffed into Intel's 10nm process far outweighed the potential benefits. Cannon Lake was also supposed to debut Gen10 Intel Graphics, but since the GPU was disabled Gen10 effectively turned into vaporware.

# Whiskey Lake (WHL, 14nm++, 8th Gen Core, August 2018)

A lesser known branch from Intel's main line of CPUs, Whiskey Lake arrived about the same time as the Coffee Lake Refresh, but focused exclusively on **mobile CPUs**. It includes the same Meltdown/Spectre hardware mitigations (many of which are still done in firmware). There are only a handful of Whiskey Lake processors, consisting primarily of 4-core/8-thread i5 and i7 models, along with one each for 2-core/4-thread Core i3 and Pentium, and 2-core/2-thread Celeron.

# Coffee Lake Refresh (CFL-R, 14nm++, 9th Gen Core, October 2018)

If the first Coffee Lake parts didn't end "Process-Architecture-Optimization," the refresh certainly did. Still using **the same 14nm++ process**, the 9th Gen Core CPUs added Core i9 branding with the 8-core/16-thread i9-9900K, along with higher boost clocks—**up to 5GHz for the first time** on an Intel CPU. Coffee Lake Refresh also adds certain hardware mitigations for the Meltdown/Spectre vulnerabilities.

# Ice Lake (ICL, 10nm+, 10th Gen Core, 2019/2020)

After the misstep of Cannon Lake and its first 10nm process technology, Intel is pressing the reset button—that's why it gets the plus sign. Ice Lake will be volume 10nm+ production, and it will potentially be the successor for Coffee Lake, Whiskey Lake, and Cannon Lake. Ice Lake is currently slated to launch on **mobile platforms** first. There's no mention in current roadmaps of Ice Lake desktop implementations, although previously there was talk of Ice Lake for servers.

At the heart of Ice Lake is the new **Sunny Cove microarchitecture**, with 2-core and 4-core mobile designs. That would make ICL more of a **true successor to the current WHL as opposed to CFL**. Ice Lake will also feature **Gen11 graphics**, and it will have a standard 64 EU design, making it Intel's first TFLOPS-class GPU. Ice Lake may also see the introduction of **PCIe Gen4** support, though that was originally listed as a server feature so it may or may not make it into mobile chips.

# Reference

[Intel CPU roadmap: all the 'Lakes' from 14nm to 7nm](https://www.pcgamer.com/intel-cpu-roadmap-all-the-lakes-from-14nm-to-7nm/)