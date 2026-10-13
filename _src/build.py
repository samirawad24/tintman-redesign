"""Builds the Tint Man concept site. Run: python _src/build.py"""
import json
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
IMG = ROOT / "assets" / "img"
EMAIL = "tintmanfl@yahoo.com"
HOME_PHONE = "321-297-9643"
FLEET_PHONE = "352-933-1903"

SHOPS = [
    dict(name="Longwood", addr="1830 Longwood Lake Mary Rd #1016", city="Longwood, FL 32750", phone="407-678-8468",
         days="Monday to Saturday. Closed Sunday.", since="Feb 2002"),
    dict(name="Winter Park", addr="6649 Amory Ct #9", city="Winter Park, FL 32792", phone="407-393-8645",
         days="7 days a week.", since="Apr 2017"),
    dict(name="Winter Garden", addr="1165 E Plant St #15", city="Winter Garden, FL 34787", phone="407-730-0494",
         days="Tuesday to Saturday. Closed Sunday and Monday.", since="Dec 2020"),
    dict(name="The Villages", addr="5732 C Thomas Rd #205", city="Wildwood, FL 34785", phone="352-933-2935",
         days="7 days a week.", since="Sep 2022"),
    dict(name="Minneola", addr="305 US Hwy 27", city="Minneola, FL 34715", phone="352-933-1903",
         days="Tuesday to Friday and Sunday. Closed Monday and Saturday.", since="Jun 2024"),
]
PRICES = dict(
    base=dict(car=dict(cs=265, xr=365, xrp=550), truck=dict(cs=265, xr=365, xrp=550), suv=dict(cs=315, xr=470, xrp=650)),
    windshield=dict(cs=180, xr=220, xrp=280), visor=dict(cs=50, xr=60, xrp=75), removeDoor=25, removeRear=150,
)


def tel(p):
    return "tel:+1" + "".join(c for c in p if c.isdigit())


def maps(s):
    q = f"Tint Man Window Tinting, {s['addr']}, {s['city']}".replace("#", "%23").replace(" ", "+")
    return "https://www.google.com/maps/search/?api=1&query=" + q


def pic(slug, alt, sizes="(max-width:860px) 100vw, 50vw", eager=False, cls=""):
    w, h = Image.open(IMG / f"{slug}.webp").size
    load = 'fetchpriority="high"' if eager else 'loading="lazy" decoding="async"'
    c = f' class="{cls}"' if cls else ""
    return (f'<img{c} src="assets/img/{slug}-800.webp" srcset="assets/img/{slug}-800.webp 800w, assets/img/{slug}.webp {w}w" '
            f'sizes="{sizes}" width="{w}" height="{h}" alt="{alt}" {load}>')


NAV = [("auto.html", "Auto prices"), ("home-office.html", "Home &amp; office"), ("fleet.html", "Fleet"),
       ("work.html", "Our work"), ("locations.html", "Locations")]


def page(fname, title, desc, body, scripts=""):
    nav = "".join(f'<a href="{h}"{" aria-current=\"page\"" if h == fname else ""}>{t}</a>' for h, t in NAV)
    shops = "".join(f'<li>{s["name"]} <a href="{tel(s["phone"])}">{s["phone"]}</a></li>' for s in SHOPS)
    html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="robots" content="noindex, nofollow">
<meta name="theme-color" content="#0e0f11">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="assets/img/og.jpg">
<meta property="og:type" content="website">
<link rel="preload" href="assets/fonts/archivo.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="assets/site.css">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="hdr">
  <div class="wrap">
    <a class="brand" href="index.html" aria-label="Tint Man, home">Tint Man</a>
    <button class="menu" type="button" aria-expanded="false" aria-controls="nav">Menu</button>
    <nav class="nav" id="nav" aria-label="Main">{nav}<a class="btn btn-p" href="auto.html#price">Get my price</a></nav>
  </div>
</header>
<main id="main">
{body}
</main>
<footer class="ftr">
  <div class="wrap">
    <div class="ftr-grid">
      <div>
        <img src="assets/img/tint-man-logo.png" width="397" height="420" alt="Tint Man logo" loading="lazy">
        <p>Tint Man FL Inc. Car, home and office window tinting in Central Florida since 2002. Licensed and insured, with workers' comp.</p>
      </div>
      <div>
        <h3>Shops, by appointment</h3>
        <ul>{shops}<li>Home and office <a href="{tel(HOME_PHONE)}">{HOME_PHONE}</a></li></ul>
      </div>
      <div>
        <h3>Services</h3>
        <ul>
          <li><a href="auto.html">Auto tint prices</a></li>
          <li><a href="home-office.html">Home and office film</a></li>
          <li><a href="fleet.html">Mobile fleet tinting</a></li>
          <li><a href="work.html">Our work</a></li>
          <li><a href="locations.html#gift">Gift certificates</a></li>
        </ul>
      </div>
      <div>
        <h3>Good to know</h3>
        <ul>
          <li><a href="tint-laws.html">Florida tint laws</a></li>
          <li><a href="warranty.html">Warranty and film care</a></li>
          <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
          <li><a href="https://www.youtube.com/channel/UCc-5ROJTFRDalu6q-zeM-1g" rel="noopener">YouTube</a></li>
          <li><a href="https://www.instagram.com/tintmanwindowtinting" rel="noopener">Instagram</a></li>
          <li><a href="https://www.facebook.com/tintmanfl" rel="noopener">Facebook</a></li>
        </ul>
      </div>
    </div>
    <div class="note">
      <span>Prices don't include Florida sales tax. Days and hours can change for holidays and family events.</span>
      <span>Concept redesign by <a class="tlink" href="https://madebyawad.com" rel="noopener">Made by Awad</a>. Not the official Tint Man site.</span>
    </div>
  </div>
</footer>
<div class="bar">
  <a class="btn btn-s" href="locations.html">Find a shop</a>
  <a class="btn btn-p" href="auto.html#price">Get my price</a>
</div>
{scripts}<script src="assets/site.js" defer></script>
</body>
</html>
"""
    assert "—" not in html and "–" not in html, f"dash in {fname}"
    (ROOT / fname).write_text(html, encoding="utf-8", newline="\n")
    print("built", fname)


def shop_rows():
    return "".join(f"""
      <div class="shop">
        <div class="nm">{s['name']}</div>
        <address>{s['addr']}, {s['city']}</address>
        <div class="dy">{s['days']}</div>
        <a class="ph" href="{tel(s['phone'])}">{s['phone']}</a>
      </div>""" for s in SHOPS)


END_CTA = """
<section class="sec end">
  <div class="wrap">
    <h2>Know your price before you call.</h2>
    <div class="btns">
      <a class="btn btn-p" href="auto.html#price">Get my price</a>
      <a class="btn btn-s" href="locations.html">Find a shop</a>
    </div>
  </div>
</section>"""

# ---------------------------------------------------------------- home
years = "".join(f"<div><b>{s['since']}</b><span>{s['name']}</span></div>" for s in SHOPS)
home = f"""
<section class="hero">
  <div class="wrap">
    <h1>Central Florida's tint shop since 2002.</h1>
    <div class="hero-row">
      <p>XPEL ceramic film, cut by computer and installed one car at a time. Five shops. Lifetime warranty.</p>
      <div class="btns">
        <a class="btn btn-p" href="auto.html#price">Get my price</a>
        <a class="btn btn-s" href="locations.html">Find a shop</a>
      </div>
    </div>
    <div class="hero-img">{pic('ferrari-red', 'Red Ferrari with fresh window tint in a Tint Man bay', '100vw', eager=True)}</div>
    <div class="proof">
      <div><b>XPEL Dealer of the Year</b>2025 Automotive Window Film, U.S. Southeast</div>
      <div><b>Best of Central FL</b>People's Choice Award winner</div>
      <div><b>Lifetime warranty</b>Nationwide, and it transfers with the car</div>
      <div><b>Licensed and insured</b>Covered by workers' comp</div>
    </div>
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <h2 class="rv">Three films. Prices up front.</h2>
    <p class="lead rv">Each price covers the side windows and rear window on most coupes and sedans. Going darker doesn't cost more.</p>
    <div class="films rv">
      <div class="film">
        <div class="nm">CS</div>
        <div class="ds mute">Color Stable dyed film. The lowest price, with 99% UV protection.</div>
        <div class="heat"><b>27%</b> <span class="mute">infrared heat rejected, up to</span></div>
        <div class="pr">$265</div>
      </div>
      <div class="film">
        <div class="nm">XR</div>
        <div class="ds mute">Black ceramic. Rejects more than three times the infrared heat of CS.</div>
        <div class="heat"><b>89%</b> <span class="mute">infrared heat rejected, up to</span></div>
        <div class="pr">$365</div>
      </div>
      <div class="film">
        <div class="nm">XR Plus</div>
        <div class="ds mute">Super ceramic, the top of XPEL's Prime line for heat rejection.</div>
        <div class="heat"><b>98%</b> <span class="mute">infrared heat rejected, up to</span></div>
        <div class="pr">$550</div>
      </div>
    </div>
    <p class="sec-foot rv"><a class="tlink" href="auto.html">Trucks, SUVs, windshields and the full price list</a></p>
  </div>
</section>

<section class="sec alt">
  <div class="wrap">
    <h2 class="rv">Cars we've tinted.</h2>
    <div class="mosaic rv">
      <a href="work.html">{pic('mclaren-blue', 'Blue McLaren in the Tint Man shop', '(max-width:760px) 100vw, 50vw')}</a>
      <a href="work.html">{pic('g-class-grey', 'Grey Mercedes G-Class with tinted windows', '(max-width:760px) 50vw, 25vw')}</a>
      <a href="work.html">{pic('rolls-royce-white', 'White Rolls-Royce SUV in a Tint Man bay', '(max-width:760px) 50vw, 25vw')}</a>
      <a href="work.html">{pic('porsche-grey', 'Grey Porsche 911 on the shop floor', '(max-width:760px) 50vw, 25vw')}</a>
      <a href="work.html">{pic('nsx-orange', 'Orange Acura NSX in a Tint Man bay', '(max-width:760px) 50vw, 25vw')}</a>
    </div>
    <p class="sec-foot rv"><a class="tlink" href="work.html">See more of our work</a></p>
  </div>
</section>

<section class="sec">
  <div class="wrap split">
    <div class="rv">{pic('plotter', 'Plotter cutting a window film pattern beside a car')}</div>
    <div class="stack rv">
      <h2>One car in the bay at a time.</h2>
      <p class="mute">We cut each pattern with XPEL software, then install it in a clean, closed, climate-controlled bay with good light. Some cars still get a hand cut, and we do those too.</p>
      <p class="mute">We work on one vehicle at a time, so yours has the tinter's full attention.</p>
      <p><a class="tlink" href="warranty.html">Warranty and film care</a></p>
    </div>
  </div>
</section>

<section class="sec alt">
  <div class="wrap duo">
    <article class="rv">
      {pic('home-estate', 'Stone-front Florida home with a work van in the driveway', '(max-width:860px) 100vw, 60vw')}
      <h2>Home and office film from $12 a square foot.</h2>
      <p>XPEL Vision film cuts heat and glare and blocks 99% of UV. Your AC runs less, and your floors and furniture keep their color. Estimates are free.</p>
      <a class="tlink" href="home-office.html">Home and office film</a>
    </article>
    <article class="rv">
      {pic('fleet-van-porsche', 'Tint Man van set up inside a client garage', '(max-width:860px) 100vw, 40vw')}
      <h2>Three or more vehicles? We come to you.</h2>
      <p>For dealerships, detail shops and fleets, we set up a tint shop in your bay for the day.</p>
      <a class="tlink" href="fleet.html">Mobile fleet tinting</a>
    </article>
  </div>
</section>

<section class="sec" id="shops">
  <div class="wrap">
    <h2 class="rv">Five shops. All by appointment.</h2>
    <p class="lead rv">Call the shop closest to you to book. Tap a number to dial.</p>
    <div class="shops rv">{shop_rows()}
    </div>
    <p class="sec-foot rv"><a class="tlink" href="locations.html">Maps and directions</a></p>
  </div>
</section>

<section class="sec alt">
  <div class="wrap split tall">
    <div class="stack rv">
      <img class="story-logo" src="assets/img/tint-man-logo.png" width="397" height="420" alt="Tint Man logo" loading="lazy">
      <h2>A family tint business since the 1990s.</h2>
      <p class="mute">Tint Man started as a mobile service run by our family. The Longwood shop opened in February 2002, and four more followed. Eight tinters work across the five shops today, with a separate crew for homes and offices.</p>
      <p><a class="tlink" href="https://youtu.be/kbAeJcgGdcU" rel="noopener">Watch our Best of Central FL feature</a></p>
    </div>
    <div class="rv">{pic('award-set', 'Two men with XPEL film displays on the Best of Central Florida set')}</div>
  </div>
  <div class="wrap"><div class="years rv">{years}</div></div>
</section>
{END_CTA}"""
page("index.html", "Tint Man FL | Car, Home and Office Window Tinting in Central Florida",
     "XPEL window tint from $265. Five Central Florida shops in Longwood, Winter Park, Winter Garden, The Villages and Minneola. Lifetime warranty. Since 2002.", home)

# ---------------------------------------------------------------- auto
shop_opts = "".join(f'<option value="{i}">{s["name"]}</option>' for i, s in enumerate(SHOPS))
auto = f"""
<section class="phead">
  <div class="wrap">
    <h1>Auto tint prices</h1>
    <p class="lead">Pick your vehicle and film. Your price updates as you go.</p>
  </div>
</section>

<section class="sec" id="price" style="padding-top:16px">
  <div class="wrap builder">
    <form id="price-form">
      <fieldset>
        <legend>Your vehicle</legend>
        <p class="hint">The price covers the side windows and the rear window.</p>
        <div class="opts c3">
          <label class="opt"><input type="radio" name="vehicle" value="car" checked><span><b>Coupe or sedan</b><small>Most models</small></span></label>
          <label class="opt"><input type="radio" name="vehicle" value="truck"><span><b>Truck</b><small>Most models</small></span></label>
          <label class="opt"><input type="radio" name="vehicle" value="suv"><span><b>SUV</b><small>Most models</small></span></label>
        </div>
      </fieldset>
      <fieldset>
        <legend>Your film</legend>
        <p class="hint">All three block 99% of UV. Going darker doesn't cost more.</p>
        <div class="opts c3">
          <label class="opt"><input type="radio" name="film" value="cs"><span><b>CS</b><small>Color Stable dyed. Up to 27% infrared heat rejected.</small></span></label>
          <label class="opt"><input type="radio" name="film" value="xr" checked><span><b>XR</b><small>Black ceramic. Up to 89% infrared heat rejected.</small></span></label>
          <label class="opt"><input type="radio" name="film" value="xrp"><span><b>XR Plus</b><small>Super ceramic. Up to 98% infrared heat rejected.</small></span></label>
        </div>
      </fieldset>
      <fieldset>
        <legend>Windshield</legend>
        <p class="hint">Florida requires a tint waiver for film below the windshield's AS-1 line.</p>
        <div class="opts c3">
          <label class="opt"><input type="radio" name="windshield" value="none" checked><span><b>None</b><small>Leave it as is</small></span></label>
          <label class="opt"><input type="radio" name="windshield" value="visor"><span><b>Visor strip</b><small>Band across the top</small></span></label>
          <label class="opt"><input type="radio" name="windshield" value="full"><span><b>Whole windshield</b><small>Waiver required</small></span></label>
        </div>
      </fieldset>
      <fieldset>
        <legend>Old tint to remove?</legend>
        <p class="hint">$25 a door and $150 for the rear window, in most cases.</p>
        <div class="opts c3">
          <div class="field"><label for="rm-doors">Doors with old tint</label>
            <select id="rm-doors" name="rm-doors"><option>0</option><option>1</option><option>2</option><option>3</option><option>4</option></select></div>
          <label class="opt"><input type="checkbox" name="rm-rear"><span><b>Rear window</b><small>Old tint on the back glass</small></span></label>
        </div>
      </fieldset>
    </form>
    <aside class="quote" aria-live="polite">
      <div class="mute">Your estimate, before tax</div>
      <div class="tot" id="q-total">$365</div>
      <ul id="q-lines"><li><span>Coupe or sedan, XR ceramic film</span><b>$365</b></li></ul>
      <div class="field"><label for="q-shop">Closest shop</label><select id="q-shop" form="price-form" name="shop">{shop_opts}</select></div>
      <a class="btn btn-p" id="q-call" href="{tel(SHOPS[0]['phone'])}">Call Longwood {SHOPS[0]['phone']}</a>
      <a class="btn btn-s" id="q-mail" href="mailto:{EMAIL}">Email this estimate</a>
      <p class="fine">Prices can vary with window size and complexity. The shop confirms your exact price when you book.</p>
    </aside>
  </div>
</section>

<section class="sec alt">
  <div class="wrap">
    <h2 class="rv">What each film does</h2>
    <p class="lead rv">All three are XPEL Prime films. None of them is a metal film, because metal can interfere with a car's electronics.</p>
    <div class="specs rv">
      <div class="spec">
        <h3>CS, Color Stable dyed</h3>
        <div class="big">27%</div><div class="mute">infrared heat rejected, up to</div>
        <dl><dt>Radiant heat rejected</dt><dd>45%</dd><dt>UV rays blocked</dt><dd>99%</dd><dt>Glare cut, up to</dt><dd>95%</dd><dt>Total solar energy rejected, up to</dt><dd>45%</dd></dl>
      </div>
      <div class="spec">
        <h3>XR, black ceramic</h3>
        <div class="big">89%</div><div class="mute">infrared heat rejected, up to</div>
        <dl><dt>Radiant heat rejected</dt><dd>66%</dd><dt>UV rays blocked</dt><dd>99%</dd><dt>Glare cut, up to</dt><dd>95%</dd><dt>Total solar energy rejected, up to</dt><dd>66%</dd></dl>
      </div>
      <div class="spec">
        <h3>XR Plus, super ceramic</h3>
        <div class="big">98%</div><div class="mute">infrared heat rejected, up to</div>
        <dl><dt>Radiant heat rejected</dt><dd>71%</dd><dt>UV rays blocked</dt><dd>99%</dd><dt>Glare cut, up to</dt><dd>95%</dd><dt>Total solar energy rejected, up to</dt><dd>71%</dd></dl>
      </div>
    </div>
    <p class="sec-foot mute small rv">Figures are XPEL's published numbers for the Prime line. See xpel.com for the full specifications.</p>
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <h2 class="rv">The full price list</h2>
    <p class="lead rv">Vehicle prices cover the side windows and rear window. A rear window on its own costs about the same as a windshield on most cars.</p>
    <div class="tbl-wrap rv">
      <table>
        <thead><tr><th scope="col">Job</th><th scope="col" class="n">CS</th><th scope="col" class="n">XR</th><th scope="col" class="n">XR Plus</th></tr></thead>
        <tbody>
          <tr><th scope="row">Most coupes and sedans</th><td class="n">$265</td><td class="n">$365</td><td class="n">$550</td></tr>
          <tr><th scope="row">Most trucks</th><td class="n">$265</td><td class="n">$365</td><td class="n">$550</td></tr>
          <tr><th scope="row">Most SUVs</th><td class="n">$315</td><td class="n">$470</td><td class="n">$650</td></tr>
          <tr><th scope="row">Whole windshield</th><td class="n">$180</td><td class="n">$220</td><td class="n">$280</td></tr>
          <tr><th scope="row">Visor strip</th><td class="n">$50</td><td class="n">$60</td><td class="n">$75</td></tr>
          <tr><th scope="row">One door</th><td class="n">$60</td><td class="n">$80</td><td class="n">$105</td></tr>
          <tr><th scope="row">Sunroof, per square foot</th><td class="n">$12</td><td class="n">$17</td><td class="n">$22</td></tr>
          <tr><th scope="row">Most RVs, per square foot</th><td class="n">$12</td><td class="n">$17</td><td class="n">$22</td></tr>
        </tbody>
      </table>
    </div>
    <p class="sec-foot mute small rv">Prices can vary with window size, complexity, material and labor. Call for an exact quote on your vehicle. Sales tax is extra.</p>
    <div class="notes rv">
      <div><h3>Old tint removal</h3><p>$25 a door and $150 for the rear window, in most cases. We steam the old film off to protect the rear defroster. It survives most removals, but we can't guarantee it.</p></div>
      <div><h3>How dark can you go?</h3><p>We carry film from 70%, the lightest, to 5%, the darkest. Darkness doesn't change the price, except 5% limo tint, which is illegal in most situations. <a class="tlink" href="tint-laws.html">Florida tint laws</a></p></div>
      <div><h3>Changing your appointment</h3><p>Give us 24 hours' notice to cancel or move it. With less notice, or if you arrive more than 15 minutes late, a $50 rescheduling fee applies, because we may not be able to fill your slot.</p></div>
      <div><h3>Gift certificates</h3><p>Tint makes a good gift. Pick one up at any shop, or call and we'll email it. <a class="tlink" href="locations.html#gift">How they work</a></p></div>
    </div>
  </div>
</section>

<section class="sec alt">
  <div class="wrap split">
    <div class="stack rv">
      <h2>Cut by computer, fitted by hand.</h2>
      <p class="mute">XPEL's software holds the window patterns for your exact vehicle. Our plotter cuts the film to those patterns, which gives the cleanest fit on most cars. A few vehicles still fit better with a hand cut, so we keep doing those too.</p>
      <p class="mute">Then we install in a clean, enclosed, climate-controlled bay, one vehicle at a time.</p>
    </div>
    <div class="video rv"><iframe src="https://www.youtube-nocookie.com/embed/i6JGkqrCtaM" title="Auto window tinting by Tint Man FL" loading="lazy" allow="accelerometer; encrypted-media; picture-in-picture" allowfullscreen></iframe></div>
  </div>
</section>
{END_CTA.replace('<a class="btn btn-p" href="auto.html#price">', '<a class="btn btn-p" href="#price">')}"""
auto_js = f"<script>window.TM_PRICES={json.dumps(PRICES)};window.TM_SHOPS={json.dumps([dict(name=s['name'], phone=s['phone']) for s in SHOPS])};</script>\n"
page("auto.html", "Auto Tint Prices | Tint Man FL",
     "Price your car, truck or SUV tint in seconds. XPEL CS from $265, XR ceramic from $365, XR Plus from $550. Lifetime warranty.", auto, auto_js)

# ---------------------------------------------------------------- home & office
FILMS = [
    ("Evening View One-Way 5%", 12, "Silver mirror on the outside, dark limo 5% on the inside.", 88, 92, 81),
    ("Dark Neutral 15%", 12, "Strong heat, glare and UV rejection without the silver exterior of other dark metal films.", 75, 90, 70),
    ("Clear View Ceramic 35%", 12, "Ceramic film that performs like traditional metal film, with no mirror look.", 83, 61, 61),
    ("Clear View Plus 70%", 22, "Close to clear. You keep the view and lose the heat.", 94, 20, 55),
    ("Clear View Plus 40%", 22, "High infrared rejection without a reflective look.", 94, 53, 62),
]
film_tiles = "".join(f"""
      <div class="spec">
        <h3>{n}</h3>
        <div class="big">${p}</div><div class="mute">per square foot</div>
        <p class="mute" style="margin-top:14px">{d}</p>
        <dl><dt>Infrared heat rejected</dt><dd>{ir}%</dd><dt>UV protection</dt><dd>99%</dd><dt>Glare reduced</dt><dd>{g}%</dd><dt>Total solar energy rejected</dt><dd>{t}%</dd></dl>
      </div>""" for n, p, d, ir, g, t in FILMS)
ho = f"""
<section class="phead">
  <div class="wrap">
    <h1>Home and office window film</h1>
    <p class="lead">XPEL Vision film cuts heat and glare and blocks 99% of UV. Your AC runs less, and your floors and furniture keep their color. Estimates are free.</p>
    <div class="btns" style="margin-top:28px">
      <a class="btn btn-p" href="{tel(HOME_PHONE)}">Call or text {HOME_PHONE}</a>
      <a class="btn btn-s" href="mailto:{EMAIL}?subject=Home%20or%20office%20film%20estimate">Email for an estimate</a>
    </div>
    <div class="hero-img">{pic('home-lakefront', 'Two-story Florida home with tinted windows', '100vw', eager=True)}</div>
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <h2 class="rv">Five popular films</h2>
    <p class="lead rv">We also carry clear, reflective, black and bronze films. Tell us the room and the problem, and we'll match a film to it.</p>
    <div class="specs five rv">{film_tiles}
    </div>
  </div>
</section>

<section class="sec alt">
  <div class="wrap">
    <h2 class="rv">Other costs to plan for</h2>
    <div class="rows rv">
      <div><b>Blackout and White Frost film</b><span>$12 per square foot. Blackout stops all light. White Frost gives privacy and keeps the daylight.</span></div>
      <div><b>Colonial squares</b><span>Around $30 per square with traditional films.</span></div>
      <div><b>Old film removal</b><span>$7 per square foot on most jobs.</span></div>
      <div><b>High windows</b><span>Extra when a window needs a lift, scaffolding or a tall ladder.</span></div>
      <div><b>Project minimum</b><span>$350 to $500 on most jobs, depending on where you are.</span></div>
    </div>
    <p class="sec-foot mute small rv">Prices don't include Florida sales tax.</p>
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <h2 class="rv">Homes, condos and offices we've done.</h2>
    <div class="strip rv">
      {pic('home-estate', 'Stone-front Florida home with a work van in the driveway', '(max-width:700px) 50vw, 33vw')}
      {pic('office-tall-glass', 'Tall office windows with a ladder set up for film install', '(max-width:700px) 50vw, 33vw')}
      {pic('installer-arched-window', 'Installer applying film to an arched window', '(max-width:700px) 50vw, 33vw')}
      {pic('home-interior', 'Installers working on upper windows inside a two-story home', '(max-width:700px) 50vw, 33vw')}
      {pic('condo-view', 'City view through a tinted high-rise condo window', '(max-width:700px) 50vw, 33vw')}
      {pic('van-at-home', 'Tint Man van parked outside a two-story home', '(max-width:700px) 50vw, 33vw')}
    </div>
  </div>
</section>

<section class="sec end">
  <div class="wrap">
    <div>
      <h2>Free estimates in four counties.</h2>
      <p class="lead">We cover most of Orange, Seminole, Lake and Sumter counties. Licensed and insured, with workers' comp.</p>
    </div>
    <div class="btns">
      <a class="btn btn-p" href="{tel(HOME_PHONE)}">Call or text {HOME_PHONE}</a>
    </div>
  </div>
</section>"""
page("home-office.html", "Home and Office Window Film | Tint Man FL",
     "XPEL Vision window film for Central Florida homes and offices from $12 a square foot. Free estimates in Orange, Seminole, Lake and Sumter counties.", ho)

# ---------------------------------------------------------------- fleet
fleet = f"""
<section class="phead">
  <div class="wrap">
    <h1>We bring the tint shop to your business.</h1>
    <p class="lead">Mobile tinting for businesses that need three or four vehicles, or more, done at a time. Fleet accounts only.</p>
    <div class="btns" style="margin-top:28px">
      <a class="btn btn-p" href="{tel(FLEET_PHONE)}">Request fleet service</a>
      <a class="btn btn-s" href="mailto:{EMAIL}?subject=Fleet%20tinting">Email us</a>
    </div>
    <div class="hero-img">{pic('fleet-van-porsche', 'Tint Man van and film plotter set up inside a client garage', '100vw', eager=True)}</div>
  </div>
</section>

<section class="sec">
  <div class="wrap split">
    <div class="stack rv">
      <h2>Your bay becomes our shop for the day.</h2>
      <p class="mute">We arrive with XPEL film, including the ceramic lines, a computer-cut plotter and laptop, our install tools and experienced installers. Your vehicles get the same work they would get at a Tint Man shop.</p>
      <p class="mute">We don't set up in a driveway to tint one vehicle. For a single car, <a class="tlink" href="locations.html">book one of our five shops</a>.</p>
    </div>
    <div class="rv">{pic('installer-cutting', 'Tint Man installer trimming film on a car window')}</div>
  </div>
</section>

<section class="sec alt">
  <div class="wrap">
    <h2 class="rv">What we need from you</h2>
    <div class="rows rv">
      <div><b>An indoor bay</b><span>Clean and enclosed, with climate control or suitable conditions.</span></div>
      <div><b>Good lighting</b><span>Our installers have to see the film edge on every window.</span></div>
      <div><b>Room to work</b><span>Enough space for our equipment next to the vehicle.</span></div>
      <div><b>A door that closes</b><span>The bay stays shut while we install, to keep dust off the glass.</span></div>
    </div>
    <h2 class="rv" style="margin-top:72px">Who books us</h2>
    <ul class="chips rv">
      <li>Dealerships</li><li>Detail shops</li><li>Automotive businesses</li><li>Fleet accounts</li><li>Exotic and collector car facilities</li><li>Companies with multiple vehicles</li>
    </ul>
    <div class="strip rv">
      {pic('fleet-garage', 'Classic Corvette in a client garage during a fleet visit', '(max-width:700px) 50vw, 33vw')}
      {pic('fleet-porsche-wall', 'Grey Porsche 911 in a client garage', '(max-width:700px) 50vw, 33vw')}
      {pic('fleet-laptop', 'Laptop and plotter set up for cutting film patterns on site', '(max-width:700px) 50vw, 33vw')}
    </div>
  </div>
</section>

<section class="sec end">
  <div class="wrap">
    <div>
      <h2>Serving fleets across Central Florida.</h2>
      <p class="lead">We cover most of Lake, Orange, Seminole and Sumter counties for qualifying fleet accounts.</p>
    </div>
    <div class="btns">
      <a class="btn btn-p" href="{tel(FLEET_PHONE)}">Call {FLEET_PHONE}</a>
    </div>
  </div>
</section>"""
page("fleet.html", "Mobile Fleet Window Tinting | Tint Man FL",
     "Tint Man brings XPEL film, a plotter and installers to your dealership, detail shop or fleet bay. Three or more vehicles at a time across Central Florida.", fleet)

# ---------------------------------------------------------------- work
WORK = [
    ('ferrari-red', 'Red Ferrari'), ('mclaren-blue', 'Blue McLaren'), ('g-class-grey', 'Grey Mercedes G-Class'),
    ('porsche-grey', 'Grey Porsche 911'), ('rolls-royce-white', 'White Rolls-Royce SUV'), ('nsx-orange', 'Orange Acura NSX'),
    ('mclaren-yellow', 'Yellow McLaren'), ('lamborghini-black', 'Black Lamborghini'), ('bmw-white', 'White BMW coupe'),
    ('chevrolet-classic', 'Maroon classic Chevrolet'), ('ferrari-yellow', 'Yellow Ferrari'), ('bentley-red', 'Red Bentley sedan'),
    ('tesla-white', 'White Tesla sedan'), ('ferrari-grey', 'Grey Ferrari'), ('bmw-suv-white', 'White BMW SUV'),
    ('porsche-side', 'Grey Porsche 911, side view'), ('bmw-i8-silver', 'Silver BMW i8 with its doors up'), ('camper-van-white', 'White camper van'),
    ('mclaren-grey', 'Grey McLaren'), ('ram-truck', 'Tan Ram pickup'), ('corvette-red', 'Red Corvette'),
    ('lucid-white', 'White Lucid sedan'), ('lamborghini-white', 'White Lamborghini convertible'), ('classic-silver', 'Silver classic sedan'),
    ('bmw-white-2', 'White BMW coupe, front view'), ('tesla-model-3', 'White Tesla Model 3'), ('installer-ferrari', 'Tint Man installer working on a white Ferrari'),
]
gal = "".join(f'<a href="assets/img/{s}.webp">{pic(s, a + " tinted at a Tint Man shop" if "installer" not in s else a, "(max-width:480px) 100vw, (max-width:900px) 50vw, 33vw", eager=i < 3)}</a>'
              for i, (s, a) in enumerate(WORK))
work = f"""
<section class="phead">
  <div class="wrap">
    <h1>Our work</h1>
    <p class="lead">Daily drivers, trucks, classics and exotics, all tinted in our own bays. Tap a photo to see it larger.</p>
  </div>
</section>
<section class="sec" style="padding-top:8px">
  <div class="wrap">
    <div class="gal">{gal}</div>
  </div>
</section>
<dialog id="lightbox" aria-label="Photo">
  <form method="dialog"><button class="btn btn-s">Close</button></form>
  <img src="" alt="">
</dialog>
{END_CTA}"""
page("work.html", "Our Work | Tint Man FL", "Photos of cars, trucks and exotics tinted with XPEL film at Tint Man's five Central Florida shops.", work)

# ---------------------------------------------------------------- locations
loc_rows = "".join(f"""
      <div class="loc">
        <h2>{s['name']}</h2>
        <address>{s['addr']}<br>{s['city']}</address>
        <p class="dy">By appointment. {s['days']}</p>
        <div class="btns">
          <a class="btn btn-p" href="{tel(s['phone'])}">Call {s['phone']}</a>
          <a class="btn btn-s" href="{maps(s)}" rel="noopener">Directions</a>
          <button class="btn btn-s" type="button" data-name="{s['name']}" data-map="Tint Man Window Tinting, {s['addr']}, {s['city']}">Show on map</button>
        </div>
      </div>""" for s in SHOPS)
first = SHOPS[0]
first_q = f"Tint Man Window Tinting, {first['addr']}, {first['city']}".replace("#", "%23").replace(" ", "+")
loc = f"""
<section class="phead">
  <div class="wrap">
    <h1>Five shops in Central Florida</h1>
    <p class="lead">Every shop works by appointment. Call the one closest to you to book.</p>
  </div>
</section>
<section class="sec" style="padding-top:8px">
  <div class="wrap locs">
    <div>{loc_rows}
    </div>
    <div class="map">
      <iframe id="map" title="Map of the selected Tint Man shop" loading="lazy" src="https://www.google.com/maps?q={first_q}&output=embed"></iframe>
      <p class="mute small">Showing: <b id="map-name">{first['name']}</b></p>
    </div>
  </div>
</section>

<section class="sec alt">
  <div class="wrap split">
    <div class="rv">{pic('lobby', 'Tint Man shop lobby with a yellow McLaren in the bay behind it')}</div>
    <div class="stack rv">
      <h2>Home, office or fleet job?</h2>
      <p class="mute">Our residential and commercial crew covers most of Orange, Seminole, Lake and Sumter counties. Call or text <a class="tlink" href="{tel(HOME_PHONE)}">{HOME_PHONE}</a> for a free estimate.</p>
      <p class="mute">For fleet service at your business, call <a class="tlink" href="{tel(FLEET_PHONE)}">{FLEET_PHONE}</a>.</p>
      <p class="mute">Prefer email? Write to <a class="tlink" href="mailto:{EMAIL}">{EMAIL}</a>.</p>
      <p class="mute small">Days and hours can change for holidays and family events.</p>
    </div>
  </div>
</section>

<section class="sec" id="gift">
  <div class="wrap">
    <h2 class="rv">Gift certificates</h2>
    <p class="lead rv">Pick one up at any shop, or call and pay by card and we'll email it to you.</p>
    <div class="rows rv">
      <div><b>Paying by phone</b><span>We take your card over the phone and give you an invoice number.</span></div>
      <div><b>The invoice number</b><span>It activates the certificate. A certificate without that number isn't valid, so keep it with the gift.</span></div>
    </div>
  </div>
</section>
{END_CTA}"""
page("locations.html", "Locations and Hours | Tint Man FL",
     "Tint Man window tinting shops in Longwood, Winter Park, Winter Garden, The Villages and Minneola. Addresses, days open, phone numbers and directions.", loc)

# ---------------------------------------------------------------- tint laws
laws = f"""
<section class="phead">
  <div class="wrap">
    <h1>Florida tint laws, in plain numbers</h1>
    <p class="lead">The percentage is how much light gets through the glass and film together. A lower number means darker glass. We carry film from 70% to 5%.</p>
  </div>
</section>
<section class="sec" style="padding-top:8px">
  <div class="wrap">
    <div class="tbl-wrap">
      <table>
        <thead><tr><th scope="col">Glass</th><th scope="col" class="n">Sedans and coupes</th><th scope="col" class="n">SUVs, vans and other multipurpose vehicles</th></tr></thead>
        <tbody>
          <tr><th scope="row">Front side windows</th><td class="n">28% or lighter</td><td class="n">28% or lighter</td></tr>
          <tr><th scope="row">Rear side windows</th><td class="n">15% or lighter</td><td class="n">6% or lighter</td></tr>
          <tr><th scope="row">Rear window</th><td class="n">15% or lighter</td><td class="n">6% or lighter</td></tr>
          <tr><th scope="row">Windshield</th><td class="n">Above the AS-1 line only</td><td class="n">Above the AS-1 line only</td></tr>
        </tbody>
      </table>
    </div>
    <div class="notes">
      <div><h3>Factory glass counts</h3><p>Your windows already carry a slight tint from the factory. An officer's meter reads the glass and the film together, so the film you choose has to leave room for it.</p></div>
      <div><h3>The windshield</h3><p>Florida allows tint above the AS-1 line, the mark near the top of the glass. Film below that line is illegal without a tint waiver.</p></div>
      <div><h3>Tint waivers</h3><p>The state grants waivers for medical reasons such as skin cancer or lupus. A doctor signs the form. <a class="tlink" href="https://www.flhsmv.gov/pdf/forms/83390.pdf" rel="noopener">Florida's waiver form (PDF)</a></p></div>
      <div><h3>The door sticker</h3><p>Florida requires a compliance sticker on the inside of the driver's door jamb.</p></div>
      <div><h3>Fines</h3><p>Police can write a ticket of up to $117 per window for illegal tint.</p></div>
      <div><h3>Banned film</h3><p>Mirrored and colored tints are illegal in Florida.</p></div>
    </div>
    <p class="sec-foot mute small">You follow the law of the state where your vehicle is registered. This page is a summary, not legal advice. Florida Statutes 316.2951 to 316.2957 hold the full rules.</p>
  </div>
</section>
{END_CTA}"""
page("tint-laws.html", "Florida Tint Laws | Tint Man FL",
     "Florida window tint limits in plain numbers: 28% on front side windows, 15% on the rear for sedans, 6% for SUVs and vans, plus windshield rules and waivers.", laws)

# ---------------------------------------------------------------- warranty
war = f"""
<section class="phead">
  <div class="wrap">
    <h1>A lifetime warranty that follows the car</h1>
    <p class="lead">Every Tint Man install comes with a free lifetime warranty. XPEL dealers honor it nationwide, and it transfers to the next owner when you sell.</p>
  </div>
</section>
<section class="sec" style="padding-top:8px">
  <div class="wrap split">
    <div class="stack">
      <h2>What it covers</h2>
      <ul class="chips"><li>Bubbling</li><li>Peeling</li><li>Flaking</li><li>Color change</li><li>Delamination</li><li>Fading</li></ul>
      <p class="mute">It doesn't cover damage from abuse, such as seatbelt nicks or ammonia-based cleaners.</p>
      <p class="mute">Keep the warranty card we hand you. It carries the roll number of your film, which lets any XPEL dealer confirm the film and handle a claim.</p>
    </div>
    <div>{pic('xpel-certificate', 'XPEL certificate naming Tint Man the 2025 Automotive Window Film Dealer of the Year, U.S. Southeast')}</div>
  </div>
</section>

<section class="sec alt">
  <div class="wrap">
    <h2 class="rv">Caring for new tint</h2>
    <div class="rows rv">
      <div><b>The first 30 days</b><span>Haze or small moisture bubbles are normal while the film dries. They clear on their own.</span></div>
      <div><b>Rolling windows down</b><span>Keep them up for two to three days.</span></div>
      <div><b>Cleaning</b><span>Wait at least five days. Skip ammonia cleaners and abrasive pads for the life of the film.</span></div>
      <div><b>Seatbelts</b><span>Guide the buckle back by hand. A buckle that swings free can nick the film on the door.</span></div>
      <div><b>Dotted glass edges</b><span>The raised dots around some windows can look milky white, because the film sits on top of the dots and air settles between them.</span></div>
    </div>
    <p class="sec-foot mute small rv">A few windows can't take film: glass with certain factory coatings, and some sunroofs and windshields that already absorb a lot of heat. Window gaskets without a felt lining can scratch film. We check for all of this before we start.</p>
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <h2 class="rv">How to inspect a finished job</h2>
    <p class="lead rv">We follow the visual inspection standard of the International Window Film Association, the trade group that sets the rules for the industry.</p>
    <div class="notes rv">
      <div><h3>On your car</h3><p>Look straight at the glass from three feet away, inside and outside, in natural daylight. Dirt specks, bubbles, creases and scratches should not stand out.</p></div>
      <div><h3>In your home or office</h3><p>Look from six feet away, from inside the room, in daylight but out of direct sun. The standard leaves out a two-inch band around the edge of the glass.</p></div>
      <div><h3>While the film dries</h3><p>Water haze and slight distortion during drying are not defects. Drying time depends on the film and the weather.</p></div>
      <div><h3>The gap at the top edge</h3><p>A gap of 1/32 to 1/16 of an inch at the top of a car window is correct. It stops the gasket from lifting the film when the window moves.</p></div>
    </div>
  </div>
</section>
{END_CTA}"""
page("warranty.html", "Warranty and Film Care | Tint Man FL",
     "Tint Man's lifetime, nationwide, transferable XPEL warranty, how to care for new window tint, and how to inspect a finished job.", war)

(ROOT / ".nojekyll").write_text("", encoding="utf-8")
