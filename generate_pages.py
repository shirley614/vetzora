import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# ===== Shared Header & Footer =====
def build_nav_html():
    groups_order = [
        "Antiparasitic APIs", "Antibacterial APIs", "Anticoccidial / Coccidiostat APIs",
        "Reproductive & Hormonal APIs", "Cardiovascular & Metabolic APIs",
        "Anti-inflammatory & Immunomodulatory APIs", "Growth Promotant APIs", "Other Veterinary APIs",
    ]
    by_group = {}
    for p in PRODUCTS:
        by_group.setdefault(p["category_group"], []).append(p)
    dropdown = ""
    for g in groups_order:
        items = by_group.get(g)
        if not items:
            continue
        dropdown += f'              <div class="dropdown-label">{g}</div>\n'
        for p in items:
            dropdown += f'              <a href="/veterinary-apis/{p["slug"]}/">{p["name"]}</a>\n'
    dropdown += '              <div class="dropdown-label" style="margin-top:8px;border-top:1px solid #e2e8f0;padding-top:8px">All Products</div>\n'
    dropdown += '              <a href="/veterinary-apis/" style="font-weight:600;color:#2563eb">View All Veterinary APIs</a>\n'
    return f'''  <header id="header" class="always-solid">
    <div class="container nav-container">
      <a href="/" class="logo">
        <span class="logo-icon">V</span>
        <span class="logo-text">Vetzora</span>
      </a>
      <nav>
        <ul class="nav-links" id="nav-links">
          <li><a href="/">Home</a></li>
          <li><a href="/about/">About Us</a></li>
          <li class="nav-dropdown">
            <span class="nav-link-text">Veterinary APIs <span class="nav-arrow">&#9662;</span></span>
            <div class="nav-dropdown-content">
{dropdown}            </div>
          </li>
          <li><a href="/blog/">Blog</a></li>
          <li><a href="/contact/">Contact Us</a></li>
        </ul>
      </nav>
      <button class="menu-toggle" id="menu-toggle" aria-label="Toggle menu">
        <span></span><span></span><span></span>
      </button>
    </div>
  </header>'''

# NAV_HTML is assigned after PRODUCTS is fully defined (see below)

FOOTER_HTML = """  <footer class="footer">
    <div class="container footer-container">
      <div class="footer-brand">
        <a href="/" class="logo">
          <span class="logo-icon">V</span>
          <span class="logo-text">Vetzora</span>
        </a>
        <p>Vetzora &mdash; Reliable Veterinary API Supply from China. Veterinary active pharmaceutical ingredients for pharmaceutical companies worldwide.</p>
      </div>
      <div class="footer-links">
        <h4>Products</h4>
        <ul>
          <li><a href="/veterinary-apis/">Veterinary APIs</a></li>
          <li><a href="/veterinary-apis/virginiamycin/">Virginiamycin</a></li>
          <li><a href="/veterinary-apis/doramectin/">Doramectin</a></li>
          <li><a href="/veterinary-apis/selamectin/">Selamectin</a></li>
        </ul>
      </div>
      <div class="footer-links">
        <h4>Company</h4>
        <ul>
          <li><a href="/">Home</a></li>
          <li><a href="/about/">About Us</a></li>
          <li><a href="/blog/">Blog</a></li>
          <li><a href="/contact/">Contact Us</a></li>
        </ul>
      </div>
      <div class="footer-contact">
        <h4>Contact</h4>
        <p>Email: info@vetzora.cn</p>
        <p>Phone: +86 19926584451</p>
        <p>Web: vetzora.cn</p>
      </div>
      <div class="footer-connect">
        <h4>Scan to Connect</h4>
        <div class="qr-grid">
          <div class="qr-card">
            <img src="/img/whatsapp-qr.svg" alt="WhatsApp QR code for Vetzora" width="92" height="92" loading="lazy">
            <span class="qr-label">WhatsApp</span>
          </div>
          <div class="qr-card">
            <img src="/img/telegram-qr.svg" alt="Telegram QR code for Vetzora" width="92" height="92" loading="lazy">
            <span class="qr-label">Telegram</span>
          </div>
        </div>
      </div>
    </div>
    <div class="footer-bottom">
      <div class="container">
        <p>&copy; 2026 Vetzora. All rights reserved. vetzora.cn</p>
      </div>
    </div>
  </footer>

  <button class="scroll-top" id="scroll-top" aria-label="Scroll to top">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M18 15l-6-6-6 6"/></svg>
  </button>

  <script src="/script.js"></script>
</body>
</html>"""

FAVICON = """  <link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><rect width='100' height='100' rx='20' fill='%232563eb'/><text x='50' y='70' text-anchor='middle' fill='%23ffffff' font-size='60' font-family='Arial' font-weight='bold'>V</text></svg>">
"""

# ===== Product Data =====
PRODUCTS = [
    {
        "slug": "virginiamycin",
        "name": "Virginiamycin",
        "category": "Antibacterial",
        "category_group": "Antibacterial APIs",
        "cas": "11006-76-1",
        "product_type": "Streptogramin Antibiotic",
        "application": "Animal Health",
        "introduction": "Virginiamycin is a streptogramin antibiotic widely used in veterinary and animal health applications. Vetzora supplies Virginiamycin raw material for veterinary pharmaceutical manufacturers and animal health companies worldwide.",
        "supply_info": "Our Virginiamycin supply is intended for qualified pharmaceutical and veterinary drug manufacturers. Product specifications, COA, technical documentation, packaging options and commercial supply conditions are available upon request.",
        "applications_text": "Vetzora provides Virginiamycin raw material for veterinary pharmaceutical manufacturers and animal health companies. Customers can request product specifications, COA and technical information for evaluation and sourcing purposes.",
        "seo_title": "Virginiamycin API Manufacturer & Supplier in China | Vetzora",
        "meta_description": "Virginiamycin API supplier from China. Vetzora provides veterinary-grade Virginiamycin for animal health and pharmaceutical applications, with technical documents and commercial supply support.",
        "faq": [
            ("What is Virginiamycin?", "Virginiamycin is a streptogramin antibiotic used in veterinary and animal health applications."),
            ("Does Vetzora supply Virginiamycin from China?", "Vetzora provides Virginiamycin sourcing and commercial supply support from China for qualified veterinary pharmaceutical customers."),
            ("Can Vetzora provide a COA for Virginiamycin?", "Yes. Product specifications and COA documentation can be provided for customer evaluation, subject to the specific product and supply arrangement."),
            ("What is the MOQ for Virginiamycin?", "MOQ depends on product specification, packaging and order quantity. Please contact Vetzora for a commercial quotation."),
            ("Can Vetzora supply Virginiamycin internationally?", "Yes. Vetzora supports international customers sourcing veterinary pharmaceutical ingredients from China."),
        ],
        "related": ["paromomycin-sulfate", "pradofloxacin"],
    },
    {
        "slug": "doramectin",
        "name": "Doramectin",
        "category": "Antiparasitic",
        "category_group": "Antiparasitic APIs",
        "cas": "117704-25-7",
        "product_type": "Macrocyclic Lactone Antiparasitic",
        "application": "Animal Health",
        "introduction": "Doramectin is a macrocyclic lactone antiparasitic agent widely used in veterinary medicine for the treatment and control of internal and external parasites in livestock and companion animals. Vetzora supplies Doramectin raw material for veterinary pharmaceutical manufacturers worldwide.",
        "supply_info": "Our Doramectin supply is intended for qualified pharmaceutical and veterinary drug manufacturers. Product specifications, COA, technical documentation, packaging options and commercial supply conditions are available upon request.",
        "applications_text": "Vetzora provides Doramectin raw material for veterinary pharmaceutical manufacturers and animal health companies. Customers can request product specifications, COA and technical information for evaluation and sourcing purposes.",
        "seo_title": "Doramectin API Manufacturer & Supplier in China | Vetzora",
        "meta_description": "Doramectin API supplier in China. Vetzora provides Doramectin raw material for veterinary pharmaceutical manufacturers and animal health applications worldwide.",
        "faq": [
            ("What is Doramectin?", "Doramectin is a macrocyclic lactone antiparasitic agent used in veterinary medicine for parasite control in companion animals and livestock."),
            ("Does Vetzora supply Doramectin from China?", "Vetzora provides Doramectin sourcing and commercial supply support from China for qualified veterinary pharmaceutical customers."),
            ("Can Vetzora provide a COA for Doramectin?", "Yes. Product specifications and COA documentation can be provided for customer evaluation, subject to the specific product and supply arrangement."),
            ("What is the MOQ for Doramectin?", "MOQ depends on product specification, packaging and order quantity. Please contact Vetzora for a commercial quotation."),
            ("Can Vetzora supply Doramectin internationally?", "Yes. Vetzora supports international customers sourcing veterinary pharmaceutical ingredients from China."),
        ],
        "related": ["selamectin", "emodepside", "milbemycin-oxime"],
    },
    {
        "slug": "selamectin",
        "name": "Selamectin",
        "category": "Antiparasitic",
        "category_group": "Antiparasitic APIs",
        "cas": "220989-52-0",
        "product_type": "Macrocyclic Lactone Antiparasitic",
        "application": "Animal Health",
        "introduction": "Selamectin is a semi-synthetic macrocyclic lactone antiparasitic agent used in veterinary medicine, particularly for companion animals. Vetzora supplies Selamectin raw material for veterinary pharmaceutical manufacturers and animal health companies worldwide.",
        "supply_info": "Our Selamectin supply is intended for qualified pharmaceutical and veterinary drug manufacturers. Product specifications, COA, technical documentation, packaging options and commercial supply conditions are available upon request.",
        "applications_text": "Vetzora provides Selamectin raw material for veterinary pharmaceutical manufacturers and animal health companies. Customers can request product specifications, COA and technical information for evaluation and sourcing purposes.",
        "seo_title": "Selamectin API Manufacturer & Supplier in China | Vetzora",
        "meta_description": "Selamectin API supplier from China. Vetzora provides Selamectin raw material for veterinary pharmaceutical and animal health manufacturers, with technical and commercial supply support.",
        "faq": [
            ("What is Selamectin?", "Selamectin is a semi-synthetic macrocyclic lactone antiparasitic agent used in veterinary medicine, particularly for companion animals."),
            ("Does Vetzora supply Selamectin from China?", "Vetzora provides Selamectin sourcing and commercial supply support from China for qualified veterinary pharmaceutical customers."),
            ("Can Vetzora provide a COA for Selamectin?", "Yes. Product specifications and COA documentation can be provided for customer evaluation, subject to the specific product and supply arrangement."),
            ("What is the MOQ for Selamectin?", "MOQ depends on product specification, packaging and order quantity. Please contact Vetzora for a commercial quotation."),
            ("Can Vetzora supply Selamectin internationally?", "Yes. Vetzora supports international customers sourcing veterinary pharmaceutical ingredients from China."),
        ],
        "related": ["doramectin", "emodepside", "derquantel"],
    },
    {
        "slug": "emodepside",
        "name": "Emodepside",
        "category": "Antiparasitic",
        "category_group": "Antiparasitic APIs",
        "cas": "155030-63-0",
        "product_type": "Cyclooctadepsipeptide Antiparasitic",
        "application": "Animal Health",
        "introduction": "Emodepside is a cyclooctadepsipeptide antiparasitic agent used in veterinary medicine for the treatment of parasitic infections in companion animals. Vetzora supplies Emodepside raw material for veterinary pharmaceutical manufacturers worldwide.",
        "supply_info": "Our Emodepside supply is intended for qualified pharmaceutical and veterinary drug manufacturers. Product specifications, COA, technical documentation, packaging options and commercial supply conditions are available upon request.",
        "applications_text": "Vetzora provides Emodepside raw material for veterinary pharmaceutical manufacturers and animal health companies. Customers can request product specifications, COA and technical information for evaluation and sourcing purposes.",
        "seo_title": "Emodepside API Manufacturer & Supplier in China | Vetzora",
        "meta_description": "Emodepside API supplier in China. Vetzora supplies Emodepside raw material for veterinary pharmaceutical manufacturers and animal health applications.",
        "faq": [
            ("What is Emodepside?", "Emodepside is a cyclooctadepsipeptide antiparasitic agent used in veterinary medicine for parasite control in companion animals."),
            ("Does Vetzora supply Emodepside from China?", "Vetzora provides Emodepside sourcing and commercial supply support from China for qualified veterinary pharmaceutical customers."),
            ("Can Vetzora provide a COA for Emodepside?", "Yes. Product specifications and COA documentation can be provided for customer evaluation, subject to the specific product and supply arrangement."),
            ("What is the MOQ for Emodepside?", "MOQ depends on product specification, packaging and order quantity. Please contact Vetzora for a commercial quotation."),
            ("Can Vetzora supply Emodepside internationally?", "Yes. Vetzora supports international customers sourcing veterinary pharmaceutical ingredients from China."),
        ],
        "related": ["doramectin", "selamectin", "milbemycin-oxime"],
    },
    {
        "slug": "paromomycin-sulfate",
        "name": "Paromomycin Sulfate",
        "category": "Antibacterial",
        "category_group": "Antibacterial APIs",
        "cas": "1263-89-4",
        "product_type": "Aminoglycoside Antibiotic",
        "application": "Animal Health",
        "introduction": "Paromomycin Sulfate is an aminoglycoside antibiotic used in veterinary and animal health applications. Vetzora provides pharmaceutical-grade Paromomycin Sulfate for veterinary and pharmaceutical manufacturing applications.",
        "supply_info": "Our Paromomycin Sulfate supply is intended for qualified pharmaceutical and veterinary drug manufacturers. Product specifications, COA, technical documentation, packaging options and commercial supply conditions are available upon request.",
        "applications_text": "Vetzora provides Paromomycin Sulfate raw material for veterinary pharmaceutical manufacturers and animal health companies. Customers can request product specifications, COA and technical information for evaluation and sourcing purposes.",
        "seo_title": "Paromomycin Sulfate API Manufacturer & Supplier | Vetzora",
        "meta_description": "Paromomycin Sulfate API supplier from China. Vetzora provides pharmaceutical-grade Paromomycin Sulfate for veterinary and pharmaceutical manufacturing applications.",
        "faq": [
            ("What is Paromomycin Sulfate?", "Paromomycin Sulfate is an aminoglycoside antibiotic used in veterinary and animal health applications."),
            ("Does Vetzora supply Paromomycin Sulfate from China?", "Vetzora provides Paromomycin Sulfate sourcing and commercial supply support from China for qualified veterinary pharmaceutical customers."),
            ("Can Vetzora provide a COA for Paromomycin Sulfate?", "Yes. Product specifications and COA documentation can be provided for customer evaluation, subject to the specific product and supply arrangement."),
            ("What is the MOQ for Paromomycin Sulfate?", "MOQ depends on product specification, packaging and order quantity. Please contact Vetzora for a commercial quotation."),
            ("Can Vetzora supply Paromomycin Sulfate internationally?", "Yes. Vetzora supports international customers sourcing veterinary pharmaceutical ingredients from China."),
        ],
        "related": ["virginiamycin", "pradofloxacin"],
    },
    {
        "slug": "pradofloxacin",
        "name": "Pradofloxacin",
        "category": "Antibacterial",
        "category_group": "Antibacterial APIs",
        "cas": "245746-40-3",
        "product_type": "Fluoroquinolone Antibiotic",
        "application": "Animal Health",
        "introduction": "Pradofloxacin is a third-generation fluoroquinolone antibiotic developed specifically for veterinary use, used for the treatment of bacterial infections in companion animals. Vetzora provides Pradofloxacin raw material for veterinary pharmaceutical manufacturers worldwide.",
        "supply_info": "Our Pradofloxacin supply is intended for qualified pharmaceutical and veterinary drug manufacturers. Product specifications, COA, technical documentation, packaging options and commercial supply conditions are available upon request.",
        "applications_text": "Vetzora provides Pradofloxacin raw material for veterinary pharmaceutical manufacturers and animal health companies. Customers can request product specifications, COA and technical information for evaluation and sourcing purposes.",
        "seo_title": "Pradofloxacin API Manufacturer & Supplier in China | Vetzora",
        "meta_description": "Pradofloxacin API supplier in China. Vetzora provides Pradofloxacin raw material for veterinary pharmaceutical manufacturers and animal health companies worldwide.",
        "faq": [
            ("What is Pradofloxacin?", "Pradofloxacin is a third-generation fluoroquinolone antibiotic developed specifically for veterinary medicine."),
            ("Does Vetzora supply Pradofloxacin from China?", "Vetzora provides Pradofloxacin sourcing and commercial supply support from China for qualified veterinary pharmaceutical customers."),
            ("Can Vetzora provide a COA for Pradofloxacin?", "Yes. Product specifications and COA documentation can be provided for customer evaluation, subject to the specific product and supply arrangement."),
            ("What is the MOQ for Pradofloxacin?", "MOQ depends on product specification, packaging and order quantity. Please contact Vetzora for a commercial quotation."),
            ("Can Vetzora supply Pradofloxacin internationally?", "Yes. Vetzora supports international customers sourcing veterinary pharmaceutical ingredients from China."),
        ],
        "related": ["virginiamycin", "paromomycin-sulfate"],
    },
    {
        "slug": "milbemycin-oxime",
        "name": "Milbemycin Oxime",
        "category": "Antiparasitic",
        "category_group": "Antiparasitic APIs",
        "cas": "119701-94-5",
        "product_type": "Macrocyclic Lactone Antiparasitic",
        "application": "Animal Health",
        "introduction": "Milbemycin Oxime is a macrocyclic lactone antiparasitic agent used in veterinary medicine for the prevention and treatment of heartworm disease and other parasitic infections in companion animals. Vetzora supplies Milbemycin Oxime raw material for veterinary pharmaceutical manufacturers worldwide.",
        "supply_info": "Our Milbemycin Oxime supply is intended for qualified pharmaceutical and veterinary drug manufacturers. Product specifications, COA, technical documentation, packaging options and commercial supply conditions are available upon request.",
        "applications_text": "Vetzora provides Milbemycin Oxime raw material for veterinary pharmaceutical manufacturers and animal health companies. Customers can request product specifications, COA and technical information for evaluation and sourcing purposes.",
        "seo_title": "Milbemycin Oxime API Manufacturer & Supplier | Vetzora",
        "meta_description": "Milbemycin Oxime API supplier from China. Vetzora provides Milbemycin Oxime raw material for veterinary pharmaceutical manufacturers and animal health applications.",
        "faq": [
            ("What is Milbemycin Oxime?", "Milbemycin Oxime is a macrocyclic lactone antiparasitic agent used in veterinary medicine for heartworm prevention and parasite control."),
            ("Does Vetzora supply Milbemycin Oxime from China?", "Vetzora provides Milbemycin Oxime sourcing and commercial supply support from China for qualified veterinary pharmaceutical customers."),
            ("Can Vetzora provide a COA for Milbemycin Oxime?", "Yes. Product specifications and COA documentation can be provided for customer evaluation, subject to the specific product and supply arrangement."),
            ("What is the MOQ for Milbemycin Oxime?", "MOQ depends on product specification, packaging and order quantity. Please contact Vetzora for a commercial quotation."),
            ("Can Vetzora supply Milbemycin Oxime internationally?", "Yes. Vetzora supports international customers sourcing veterinary pharmaceutical ingredients from China."),
        ],
        "related": ["doramectin", "selamectin", "emodepside"],
    },
    {
        "slug": "derquantel",
        "name": "Derquantel",
        "category": "Antiparasitic",
        "category_group": "Antiparasitic APIs",
        "cas": "187664-31-7",
        "product_type": "Spiroindoline Antiparasitic",
        "application": "Animal Health",
        "introduction": "Derquantel is a spiroindoline antiparasitic agent used in veterinary medicine, particularly for the treatment of parasitic nematode infections in livestock. Vetzora supplies Derquantel raw material for veterinary pharmaceutical manufacturers and animal health companies worldwide.",
        "supply_info": "Our Derquantel supply is intended for qualified pharmaceutical and veterinary drug manufacturers. Product specifications, COA, technical documentation, packaging options and commercial supply conditions are available upon request.",
        "applications_text": "Vetzora provides Derquantel raw material for veterinary pharmaceutical manufacturers and animal health companies. Customers can request product specifications, COA and technical information for evaluation and sourcing purposes.",
        "seo_title": "Derquantel API Manufacturer & Supplier in China | Vetzora",
        "meta_description": "Derquantel API supplier from China. Vetzora provides Derquantel raw material for veterinary pharmaceutical and animal health applications.",
        "faq": [
            ("What is Derquantel?", "Derquantel is a spiroindoline antiparasitic agent used in veterinary medicine for nematode control in livestock."),
            ("Does Vetzora supply Derquantel from China?", "Vetzora provides Derquantel sourcing and commercial supply support from China for qualified veterinary pharmaceutical customers."),
            ("Can Vetzora provide a COA for Derquantel?", "Yes. Product specifications and COA documentation can be provided for customer evaluation, subject to the specific product and supply arrangement."),
            ("What is the MOQ for Derquantel?", "MOQ depends on product specification, packaging and order quantity. Please contact Vetzora for a commercial quotation."),
            ("Can Vetzora supply Derquantel internationally?", "Yes. Vetzora supports international customers sourcing veterinary pharmaceutical ingredients from China."),
        ],
        "related": ["doramectin", "selamectin", "emodepside"],
    },
    {
        "slug": "narasin",
        "name": "Narasin",
        "category": "Other",
        "category_group": "Other Veterinary APIs",
        "cas": "58331-04-3",
        "product_type": "Ionophore Antibiotic",
        "application": "Animal Health",
        "introduction": "Narasin is an ionophore antibiotic used in veterinary and animal health applications, particularly as a feed additive for poultry and livestock. Vetzora supplies Narasin for veterinary pharmaceutical and animal health applications.",
        "supply_info": "Our Narasin supply is intended for qualified pharmaceutical and veterinary drug manufacturers. Product specifications, COA, technical documentation, packaging options and commercial supply conditions are available upon request.",
        "applications_text": "Vetzora provides Narasin raw material for veterinary pharmaceutical manufacturers and animal health companies. Customers can request product specifications, COA and technical information for evaluation and sourcing purposes.",
        "seo_title": "Narasin API Manufacturer & Supplier in China | Vetzora",
        "meta_description": "Narasin supplier from China for veterinary pharmaceutical and animal health applications. Contact Vetzora for product specifications and commercial supply.",
        "faq": [
            ("What is Narasin?", "Narasin is an ionophore antibiotic used in veterinary and animal health applications, particularly as a feed additive."),
            ("Does Vetzora supply Narasin from China?", "Vetzora provides Narasin sourcing and commercial supply support from China for qualified veterinary pharmaceutical customers."),
            ("Can Vetzora provide a COA for Narasin?", "Yes. Product specifications and COA documentation can be provided for customer evaluation, subject to the specific product and supply arrangement."),
            ("What is the MOQ for Narasin?", "MOQ depends on product specification, packaging and order quantity. Please contact Vetzora for a commercial quotation."),
            ("Can Vetzora supply Narasin internationally?", "Yes. Vetzora supports international customers sourcing veterinary pharmaceutical ingredients from China."),
        ],
        "related": ["lasalocid-sodium", "virginiamycin"],
    },
    {
        "slug": "lasalocid-sodium",
        "name": "Lasalocid Sodium",
        "category": "Other",
        "category_group": "Other Veterinary APIs",
        "cas": "25999-20-6",
        "product_type": "Ionophore Antibiotic",
        "application": "Animal Health",
        "introduction": "Lasalocid Sodium is an ionophore antibiotic used in veterinary and animal health applications, particularly as a feed additive for poultry and cattle. Vetzora provides Lasalocid Sodium for animal health and veterinary pharmaceutical applications.",
        "supply_info": "Our Lasalocid Sodium supply is intended for qualified pharmaceutical and veterinary drug manufacturers. Product specifications, COA, technical documentation, packaging options and commercial supply conditions are available upon request.",
        "applications_text": "Vetzora provides Lasalocid Sodium raw material for veterinary pharmaceutical manufacturers and animal health companies. Customers can request product specifications, COA and technical information for evaluation and sourcing purposes.",
        "seo_title": "Lasalocid Sodium API Manufacturer & Supplier | Vetzora",
        "meta_description": "Lasalocid Sodium supplier from China for animal health and veterinary pharmaceutical applications. Vetzora provides technical documentation and commercial sourcing support.",
        "faq": [
            ("What is Lasalocid Sodium?", "Lasalocid Sodium is an ionophore antibiotic used in veterinary and animal health applications, particularly as a feed additive."),
            ("Does Vetzora supply Lasalocid Sodium from China?", "Vetzora provides Lasalocid Sodium sourcing and commercial supply support from China for qualified veterinary pharmaceutical customers."),
            ("Can Vetzora provide a COA for Lasalocid Sodium?", "Yes. Product specifications and COA documentation can be provided for customer evaluation, subject to the specific product and supply arrangement."),
            ("What is the MOQ for Lasalocid Sodium?", "MOQ depends on product specification, packaging and order quantity. Please contact Vetzora for a commercial quotation."),
            ("Can Vetzora supply Lasalocid Sodium internationally?", "Yes. Vetzora supports international customers sourcing veterinary pharmaceutical ingredients from China."),
        ],
        "related": ["narasin", "virginiamycin"],
    },
]

# ===== New Products (added per request) =====
def make_product(slug, name, category, category_group, product_type, cas=None, related=None):
    related = related or []
    intro = (f"{name} is a {product_type.lower()} used in veterinary medicine and animal health "
             f"applications. Vetzora supplies {name} raw material for veterinary pharmaceutical manufacturers "
             f"and animal health companies worldwide.")
    supply = (f"Our {name} supply is intended for qualified pharmaceutical and veterinary drug manufacturers. "
              f"Product specifications, COA, technical documentation, packaging options and commercial supply "
              f"conditions are available upon request.")
    apps = (f"Vetzora provides {name} raw material for veterinary pharmaceutical manufacturers and animal health "
            f"companies. Customers can request product specifications, COA and technical information for evaluation "
            f"and sourcing purposes.")
    seo_title = f"{name} API Manufacturer & Supplier in China | Vetzora"
    meta = (f"{name} API supplier from China. Vetzora provides {name} ({product_type}) for veterinary pharmaceutical "
            f"and animal health applications, with technical and commercial supply support.")
    faq = [
        (f"What is {name}?", f"{name} is a {product_type.lower()} used in veterinary medicine and animal health applications."),
        (f"Does Vetzora supply {name} from China?", f"Vetzora provides {name} sourcing and commercial supply support from China for qualified veterinary pharmaceutical customers."),
        (f"Can Vetzora provide a COA for {name}?", "Yes. Product specifications and COA documentation can be provided for customer evaluation, subject to the specific product and supply arrangement."),
        (f"What is the MOQ for {name}?", "MOQ depends on product specification, packaging and order quantity. Please contact Vetzora for a commercial quotation."),
        (f"Can Vetzora supply {name} internationally?", "Yes. Vetzora supports international customers sourcing veterinary pharmaceutical ingredients from China."),
    ]
    return {
        "slug": slug, "name": name, "category": category, "category_group": category_group,
        "cas": cas, "product_type": product_type, "application": "Animal Health",
        "introduction": intro, "supply_info": supply, "applications_text": apps,
        "seo_title": seo_title, "meta_description": meta, "faq": faq, "related": related,
    }

NEW_PRODUCTS = [
    # Antiparasitic APIs
    make_product("fluralaner", "Fluralaner", "Antiparasitic", "Antiparasitic APIs", "Isoxazoline Ectoparasiticide"),
    make_product("moxidectin", "Moxidectin", "Antiparasitic", "Antiparasitic APIs", "Macrocyclic Lactone Antiparasitic"),
    make_product("fipronil", "Fipronil", "Antiparasitic", "Antiparasitic APIs", "Phenylpyrazole Ectoparasiticide"),
    make_product("flumethrin", "Flumethrin", "Antiparasitic", "Antiparasitic APIs", "Pyrethroid Ectoparasiticide"),
    make_product("monepantel", "Monepantel", "Antiparasitic", "Antiparasitic APIs", "Amino-acetonitrile Derivative (AAD) Anthelmintic"),
    # Antibacterial APIs
    make_product("valnemulin-hydrochloride", "Valnemulin Hydrochloride", "Antibacterial", "Antibacterial APIs", "Pleuromutilin Antibiotic"),
    make_product("tulathromycin", "Tulathromycin", "Antibacterial", "Antibacterial APIs", "Macrolide Antibiotic"),
    # Anticoccidial / Coccidiostat APIs
    make_product("toltrazuril", "Toltrazuril", "Anticoccidial", "Anticoccidial / Coccidiostat APIs", "Triazinone Coccidiostat"),
    make_product("ponazuril", "Ponazuril", "Anticoccidial", "Anticoccidial / Coccidiostat APIs", "Triazinone Coccidiostat"),
    make_product("diclazuril", "Diclazuril", "Anticoccidial", "Anticoccidial / Coccidiostat APIs", "Benzeneacetonitrile Coccidiostat (Pure & Premix)"),
    make_product("decoquinate", "Decoquinate", "Anticoccidial", "Anticoccidial / Coccidiostat APIs", "Quinolone Coccidiostat (Pure & Premix)"),
    # Reproductive & Hormonal APIs
    make_product("chorionic-gonadotrophin-hcg", "Chorionic Gonadotrophin (HCG)", "Hormonal", "Reproductive & Hormonal APIs", "Gonadotropin Hormone"),
    make_product("serum-gonadotrophin-pmsg", "Serum Gonadotrophin (PMSG)", "Hormonal", "Reproductive & Hormonal APIs", "Gonadotropin Hormone"),
    make_product("cloprostenol-sodium", "Cloprostenol Sodium", "Hormonal", "Reproductive & Hormonal APIs", "Prostaglandin Analog (Luteolytic)"),
    make_product("d-cloprostenol-sodium", "D-Cloprostenol Sodium", "Hormonal", "Reproductive & Hormonal APIs", "Prostaglandin Analog (Luteolytic)"),
    make_product("altrenogest", "Altrenogest", "Hormonal", "Reproductive & Hormonal APIs", "Synthetic Progestogen"),
    make_product("dinoprost-trometamol", "Dinoprost Trometamol", "Hormonal", "Reproductive & Hormonal APIs", "Prostaglandin F2alpha Preparation"),
    make_product("dinoprost", "Dinoprost", "Hormonal", "Reproductive & Hormonal APIs", "Prostaglandin F2alpha"),
    make_product("denaverine-hydrochloride", "Denaverine Hydrochloride", "Hormonal", "Reproductive & Hormonal APIs", "Spasmolytic / Tocolytic Agent"),
    make_product("oxytocin", "Oxytocin", "Hormonal", "Reproductive & Hormonal APIs", "Pituitary Peptide Hormone"),
    make_product("carbetocin", "Carbetocin", "Hormonal", "Reproductive & Hormonal APIs", "Long-acting Oxytocin Analog"),
    make_product("alarelin-acetate", "Alarelin Acetate", "Hormonal", "Reproductive & Hormonal APIs", "GnRH Agonist (Analog)"),
    make_product("gonadorelin-acetate", "Gonadorelin Acetate", "Hormonal", "Reproductive & Hormonal APIs", "GnRH Agonist"),
    make_product("triptorelin-acetate", "Triptorelin Acetate", "Hormonal", "Reproductive & Hormonal APIs", "GnRH Agonist"),
    make_product("lecirelin-acetate", "Lecirelin Acetate", "Hormonal", "Reproductive & Hormonal APIs", "GnRH Agonist"),
    make_product("deslorelin-acetate", "Deslorelin Acetate", "Hormonal", "Reproductive & Hormonal APIs", "GnRH Agonist"),
    make_product("buserelin-acetate", "Buserelin Acetate", "Hormonal", "Reproductive & Hormonal APIs", "GnRH Agonist"),
    # Cardiovascular & Metabolic APIs
    make_product("pimobendan", "Pimobendan", "Cardiovascular", "Cardiovascular & Metabolic APIs", "Inodilator (PDE-III/IV Inhibitor)"),
    make_product("trilostane", "Trilostane", "Cardiovascular", "Cardiovascular & Metabolic APIs", "Steroid Synthesis Inhibitor (3beta-HSD)"),
    make_product("menbuton", "Menbuton", "Cardiovascular", "Cardiovascular & Metabolic APIs", "Choleretic / Hepatobiliary Agent"),
    # Anti-inflammatory & Immunomodulatory APIs
    make_product("oclacitinib-maleate", "Oclacitinib Maleate", "Anti-inflammatory", "Anti-inflammatory & Immunomodulatory APIs", "Janus Kinase (JAK) Inhibitor"),
    # Growth Promotant APIs
    make_product("zilpaterol-hcl", "Zilpaterol HCl", "Growth Promotant", "Growth Promotant APIs", "Beta-2 Agonist (Growth Promotant)"),
]

PRODUCTS.extend(NEW_PRODUCTS)
NAV_HTML = build_nav_html()

def get_product_by_slug(slug):
    for p in PRODUCTS:
        if p["slug"] == slug:
            return p
    return None

# ===== Product Page Template =====
def generate_product_page(p):
    related_products = [get_product_by_slug(s) for s in p["related"] if get_product_by_slug(s)]

    faq_html = ""
    if p.get("faq"):
        faq_items = ""
        for q, a in p["faq"]:
            faq_items += f"""          <div class="faq-item">
            <div class="faq-question">{q}<span class="faq-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M6 9l6 6 6-6"/></svg></span></div>
            <div class="faq-answer"><div class="faq-answer-inner">{a}</div></div>
          </div>
"""
        faq_html = f"""      <h2>Frequently Asked Questions</h2>
      <div class="faq-section">
{faq_items}      </div>"""

    related_html = ""
    if related_products:
        cards = ""
        for rp in related_products:
            cards += f"""          <a href="/veterinary-apis/{rp['slug']}/" class="internal-link-card">
            <h4>{rp['name']}</h4>
            <p>{rp['category_group']}</p>
          </a>
"""
        related_html = f"""      <h2>Related Veterinary APIs</h2>
      <div class="internal-links">
{cards}      </div>"""

    faq_schema = ""
    if p.get("faq"):
        faq_entities = ""
        for q, a in p["faq"]:
            faq_entities += f'{{"@type":"Question","name":"{q}","acceptedAnswer":{{"@type":"Answer","text":"{a}"}}}},'
        faq_entities = faq_entities.rstrip(',')
        faq_schema = f""",{{"@type":"FAQPage","mainEntity":[{faq_entities}]}}"""

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{p['seo_title']}</title>
  <meta name="description" content="{p['meta_description']}">
  <link rel="canonical" href="https://vetzora.cn/veterinary-apis/{p['slug']}/">
  <meta name="robots" content="index, follow">
  <meta property="og:type" content="product">
  <meta property="og:title" content="{p['seo_title']}">
  <meta property="og:description" content="{p['meta_description']}">
  <meta property="og:url" content="https://vetzora.cn/veterinary-apis/{p['slug']}/">
{FAVICON}  <link rel="stylesheet" href="/style.css">
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@graph": [
      {{
        "@type": "Product",
        "name": "{p['name']} API",
        "description": "{p['introduction']}",
        "category": "Veterinary API",
        "url": "https://vetzora.cn/veterinary-apis/{p['slug']}/"
      }},
      {{
        "@type": "BreadcrumbList",
        "itemListElement": [
          {{"@type":"ListItem","position":1,"name":"Home","item":"https://vetzora.cn/"}},
          {{"@type":"ListItem","position":2,"name":"Veterinary APIs","item":"https://vetzora.cn/veterinary-apis/"}},
          {{"@type":"ListItem","position":3,"name":"{p['name']}","item":"https://vetzora.cn/veterinary-apis/{p['slug']}/"}}
        ]
      }}
    ]
  }}
  </script>
</head>
<body>

{NAV_HTML}

  <section class="page-hero">
    <div class="hero-pattern"></div>
    <div class="container page-hero-content">
      <h1>{p['name']} API</h1>
      <p class="page-subtitle">{p['name']} Manufacturer &amp; Supplier in China</p>
      <p class="page-description">{p['introduction']}</p>
      <div class="hero-actions" style="margin-top:24px">
        <a href="/contact/" class="btn btn-primary">Request a Quote</a>
        <a href="/veterinary-apis/" class="btn btn-outline">All Veterinary APIs</a>
      </div>
    </div>
  </section>

  <nav class="breadcrumbs">
    <div class="container">
      <ol>
        <li><a href="/">Home</a></li>
        <li><a href="/veterinary-apis/">Veterinary APIs</a></li>
        <li>{p['name']}</li>
      </ol>
    </div>
  </nav>

  <section class="product-detail">
    <div class="container">
      <div class="product-detail-content">
        <div class="product-detail-main">
          <h2>{p['name']} Product Information</h2>
          <table class="info-table">
            <tr><th>Product Name</th><td>{p['name']}</td></tr>
            <tr><th>CAS No.</th><td>{p.get('cas', 'Available upon request')}</td></tr>
            <tr><th>Product Type</th><td>{p['product_type']}</td></tr>
            <tr><th>Category</th><td>Veterinary API</td></tr>
            <tr><th>Application</th><td>{p['application']}</td></tr>
            <tr><th>Grade</th><td>Veterinary / Pharmaceutical Grade</td></tr>
            <tr><th>Documentation</th><td>COA / Technical Documents</td></tr>
            <tr><th>Packaging</th><td>Customized</td></tr>
            <tr><th>Supply</th><td>Commercial Quantity</td></tr>
            <tr><th>Origin</th><td>China</td></tr>
          </table>

          <h2>{p['name']} for Veterinary Pharmaceutical Manufacturing</h2>
          <p>{p['applications_text']}</p>
          <p>{p['supply_info']}</p>

          <h2>Why Source {p['name']} from Vetzora?</h2>
          <ul>
            <li>China-based supply</li>
            <li>Veterinary API sourcing</li>
            <li>Commercial quantity supply</li>
            <li>Technical documentation support</li>
            <li>Flexible packaging options</li>
            <li>International export experience</li>
            <li>Direct communication with the Vetzora team</li>
          </ul>

{faq_html}

{related_html}

          <div style="margin-top:48px;padding:32px;background:var(--color-accent-bg);border-radius:var(--radius-lg);text-align:center">
            <h2 style="margin-top:0">Request {p['name']} Information</h2>
            <p style="color:var(--color-text-muted);margin-bottom:20px">Contact Vetzora for product specifications, COA, pricing and commercial supply.</p>
            <a href="/contact/" class="btn btn-primary">Contact Our Team</a>
          </div>
        </div>

        <aside class="product-sidebar">
          <h3>Need {p['name']}?</h3>
          <p>Request product specifications, COA and commercial quotation from Vetzora.</p>
          <a href="/contact/" class="btn btn-primary">Request a Quote</a>
          <a href="mailto:info@vetzora.cn" class="btn btn-dark" style="margin-top:8px">Email Us</a>
          <div style="margin-top:24px;padding-top:20px;border-top:1px solid var(--color-border)">
            <p style="font-size:13px"><strong>Phone:</strong><br>+86 19926584451</p>
            <p style="font-size:13px;margin-top:8px"><strong>Email:</strong><br>info@vetzora.cn</p>
          </div>
        </aside>
      </div>
    </div>
  </section>

{FOOTER_HTML}"""
    return html

# ===== Generate Product Pages =====
for p in PRODUCTS:
    dir_path = os.path.join(BASE_DIR, "veterinary-apis", p["slug"])
    os.makedirs(dir_path, exist_ok=True)
    file_path = os.path.join(dir_path, "index.html")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(generate_product_page(p))
    print(f"Generated: veterinary-apis/{p['slug']}/index.html")

# ===== Veterinary APIs Category Page =====
category_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Veterinary APIs &mdash; Product Catalog | Vetzora</title>
  <meta name="description" content="Vetzora's veterinary API catalog includes antiparasitic APIs, antibacterial APIs and other veterinary pharmaceutical ingredients for animal health manufacturers worldwide.">
  <link rel="canonical" href="https://vetzora.cn/veterinary-apis/">
  <meta name="robots" content="index, follow">
{FAVICON}  <link rel="stylesheet" href="/style.css">
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "BreadcrumbList",
    "itemListElement": [
      {{"@type":"ListItem","position":1,"name":"Home","item":"https://vetzora.cn/"}},
      {{"@type":"ListItem","position":2,"name":"Veterinary APIs","item":"https://vetzora.cn/veterinary-apis/"}}
    ]
  }}
  </script>
</head>
<body>

{NAV_HTML}

  <section class="page-hero">
    <div class="hero-pattern"></div>
    <div class="container page-hero-content">
      <h1>Veterinary APIs</h1>
      <p class="page-subtitle">Veterinary Active Pharmaceutical Ingredients</p>
      <p class="page-description">Vetzora supplies veterinary active pharmaceutical ingredients covering antiparasitic, antibacterial and other categories for animal health manufacturers worldwide.</p>
    </div>
  </section>

  <nav class="breadcrumbs">
    <div class="container">
      <ol>
        <li><a href="/">Home</a></li>
        <li>Veterinary APIs</li>
      </ol>
    </div>
  </nav>

  <section class="products-section" style="background:var(--color-bg)">
    <div class="container">
"""

# Group products by category
groups = {}
for p in PRODUCTS:
    g = p["category_group"]
    if g not in groups:
        groups[g] = []
    groups[g].append(p)

for group_name, products in groups.items():
    category_html += f'      <div class="product-category-group">\n        <h3>{group_name}</h3>\n        <div class="product-grid">\n'
    for p in products:
        category_html += f'          <a href="/veterinary-apis/{p["slug"]}/" class="product-card">\n'
        category_html += f'            <h4>{p["name"]}</h4>\n'
        category_html += f'            <p>{p["product_type"]}</p>\n'
        category_html += f'            <span class="product-link">View Details &rarr;</span>\n'
        category_html += f'          </a>\n'
    category_html += '        </div>\n      </div>\n'

category_html += f"""    </div>
  </section>

  <section class="seo-text-section">
    <div class="container">
      <h2>Veterinary API Supplier from China</h2>
      <p>Vetzora is a China-based veterinary API supplier providing active pharmaceutical ingredients for animal health applications. Our product portfolio covers antiparasitic APIs, antibacterial APIs, anticoccidial / coccidiostat APIs, reproductive &amp; hormonal APIs, cardiovascular &amp; metabolic APIs, anti-inflammatory &amp; immunomodulatory APIs and growth promotant APIs for companion animals, livestock and animal health manufacturers worldwide.</p>
      <p>We support international customers with product specifications, COA documentation, technical information and commercial supply solutions. Contact Vetzora for veterinary API sourcing from China.</p>
    </div>
  </section>

  <div style="text-align:center;padding:60px 0;background:var(--color-bg-alt)">
    <div class="container">
      <a href="/contact/" class="btn btn-primary">Request Product Information</a>
    </div>
  </div>

{FOOTER_HTML}"""

with open(os.path.join(BASE_DIR, "veterinary-apis", "index.html"), "w", encoding="utf-8") as f:
    f.write(category_html)
print("Generated: veterinary-apis/index.html")

# ===== About Page =====
about_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>About Vetzora &mdash; Veterinary API Supplier in China</title>
  <meta name="description" content="Vetzora is a China-based veterinary API manufacturer and supplier, providing veterinary active pharmaceutical ingredients for pharmaceutical companies worldwide.">
  <link rel="canonical" href="https://vetzora.cn/about/">
  <meta name="robots" content="index, follow">
{FAVICON}  <link rel="stylesheet" href="/style.css">
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@graph": [
      {{
        "@type": "AboutPage",
        "name": "About Vetzora",
        "url": "https://vetzora.cn/about/",
        "publisher": {{
          "@type": "Organization",
          "name": "Vetzora",
          "url": "https://vetzora.cn/",
          "email": "info@vetzora.cn",
          "telephone": "+86 19926584451",
          "description": "China-based veterinary API manufacturer and supplier providing veterinary active pharmaceutical ingredients worldwide."
        }}
      }},
      {{
        "@type": "BreadcrumbList",
        "itemListElement": [
          {{"@type":"ListItem","position":1,"name":"Home","item":"https://vetzora.cn/"}},
          {{"@type":"ListItem","position":2,"name":"About","item":"https://vetzora.cn/about/"}}
        ]
      }}
    ]
  }}
  </script>
</head>
<body>

{NAV_HTML}

  <section class="page-hero">
    <div class="hero-pattern"></div>
    <div class="container page-hero-content">
      <h1>About Vetzora</h1>
      <p class="page-subtitle">Veterinary API Manufacturer &amp; Supplier from China</p>
      <p class="page-description">Vetzora is a China-based supplier specializing in veterinary active pharmaceutical ingredients.</p>
    </div>
  </section>

  <nav class="breadcrumbs">
    <div class="container">
      <ol>
        <li><a href="/">Home</a></li>
        <li>About Us</li>
      </ol>
    </div>
  </nav>

  <section class="about" style="padding-top:60px">
    <div class="container">
      <div class="about-content">
        <div class="about-text">
          <p><strong>Vetzora is a China-based supplier specializing in veterinary active pharmaceutical ingredients (Veterinary APIs).</strong></p>
          <p>We work with pharmaceutical manufacturers, veterinary drug companies, distributors and sourcing partners worldwide, providing reliable access to pharmaceutical-grade raw materials from China.</p>
          <p>Our veterinary API portfolio covers products for companion animals, livestock and animal health applications, including antiparasitic, antibacterial and other veterinary pharmaceutical ingredients.</p>
          <p>With a focus on quality, supply stability and international business support, Vetzora works with customers from initial product sourcing through commercial supply.</p>
          <ul class="about-list">
            <li>Veterinary API sourcing and supply</li>
            <li>COA and technical documentation</li>
            <li>Commercial quantity supply</li>
            <li>International export experience</li>
            <li>Flexible packaging options</li>
          </ul>
        </div>
        <div class="about-features">
          <div class="feature-card">
            <div class="feature-icon">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2L4 5v6c0 5 3.5 9 8 11 4.5-2 8-6 8-11V5l-8-3z"/><path d="M9 12l2 2 4-4"/></svg>
            </div>
            <h3>Quality Assurance</h3>
            <p>Product specifications, COA and technical documentation available for all products.</p>
          </div>
          <div class="feature-card">
            <div class="feature-icon">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="9"/><path d="M3 12h18"/><path d="M12 3a15 15 0 010 18"/><path d="M12 3a15 15 0 000 18"/></svg>
            </div>
            <h3>Global Supply</h3>
            <p>Serving pharmaceutical companies across continents with international export experience.</p>
          </div>
          <div class="feature-card">
            <div class="feature-icon">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 00-2 2v16a2 2 0 002 2h12a2 2 0 002-2V8z"/><path d="M14 2v6h6"/><path d="M9 13l2 2 4-4"/></svg>
            </div>
            <h3>Documentation Support</h3>
            <p>Product specifications, COA, technical information and commercial supply documentation.</p>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section class="seo-text-section">
    <div class="container">
      <h2>China Veterinary API Supplier</h2>
      <p>Vetzora supplies veterinary active pharmaceutical ingredients to pharmaceutical manufacturers and animal health companies worldwide. Our portfolio includes antiparasitic APIs, antibacterial APIs and other veterinary pharmaceutical ingredients used in the development and manufacture of veterinary medicines.</p>
      <p>We support international customers with product specifications, COA documentation, technical information, samples and commercial supply solutions. For customers looking for reliable veterinary API suppliers in China, Vetzora provides direct sourcing support and international export services.</p>
    </div>
  </section>

  <div style="text-align:center;padding:60px 0;background:var(--color-bg-alt)">
    <div class="container">
      <a href="/veterinary-apis/" class="btn btn-dark">View Veterinary APIs</a>
      <a href="/contact/" class="btn btn-primary" style="margin-left:12px">Contact Us</a>
    </div>
  </div>

{FOOTER_HTML}"""

with open(os.path.join(BASE_DIR, "about", "index.html"), "w", encoding="utf-8") as f:
    f.write(about_html)
print("Generated: about/index.html")

# ===== Contact Page =====
contact_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Contact Vetzora &mdash; Veterinary API Supplier</title>
  <meta name="description" content="Contact Vetzora for veterinary API product specifications, COA, pricing and commercial supply. Email: info@vetzora.cn, Phone: +86 19926584451.">
  <link rel="canonical" href="https://vetzora.cn/contact/">
  <meta name="robots" content="index, follow">
{FAVICON}  <link rel="stylesheet" href="/style.css">
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@graph": [
      {{
        "@type": "ContactPage",
        "name": "Contact Vetzora",
        "url": "https://vetzora.cn/contact/",
        "publisher": {{
          "@type": "Organization",
          "name": "Vetzora",
          "url": "https://vetzora.cn/",
          "email": "info@vetzora.cn",
          "telephone": "+86 19926584451",
          "contactPoint": {{
            "@type": "ContactPoint",
            "telephone": "+86 19926584451",
            "email": "info@vetzora.cn",
            "contactType": "sales",
            "areaServed": "Worldwide"
          }}
        }}
      }},
      {{
        "@type": "BreadcrumbList",
        "itemListElement": [
          {{"@type":"ListItem","position":1,"name":"Home","item":"https://vetzora.cn/"}},
          {{"@type":"ListItem","position":2,"name":"Contact","item":"https://vetzora.cn/contact/"}}
        ]
      }}
    ]
  }}
  </script>
</head>
<body>

{NAV_HTML}

  <section class="page-hero">
    <div class="hero-pattern"></div>
    <div class="container page-hero-content">
      <h1>Contact Us</h1>
      <p class="page-subtitle">Get in Touch with Vetzora</p>
      <p class="page-description">Interested in our veterinary APIs? Contact our team for product specifications, COA and commercial supply.</p>
    </div>
  </section>

  <nav class="breadcrumbs">
    <div class="container">
      <ol>
        <li><a href="/">Home</a></li>
        <li>Contact Us</li>
      </ol>
    </div>
  </nav>

  <section class="contact-section">
    <div class="container">
      <div class="contact-content">
        <div class="contact-info">
          <div class="contact-item">
            <div class="contact-icon">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="4" width="20" height="16" rx="2"/><path d="M22 7l-10 6L2 7"/></svg>
            </div>
            <div class="contact-detail">
              <h4>Email</h4>
              <p>info@vetzora.cn</p>
            </div>
          </div>
          <div class="contact-item">
            <div class="contact-icon">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.92v3a2 2 0 01-2.18 2 19.79 19.79 0 01-8.63-3.07 19.5 19.5 0 01-6-6 19.79 19.79 0 01-3.07-8.67A2 2 0 014.11 2h3a2 2 0 012 1.72c.13.96.36 1.9.7 2.81a2 2 0 01-.45 2.11L8.09 9.91a16 16 0 006 6l1.27-1.27a2 2 0 012.11-.45c.91.34 1.85.57 2.81.7A2 2 0 0122 16.92z"/></svg>
            </div>
            <div class="contact-detail">
              <h4>Phone</h4>
              <p>+86 19926584451</p>
            </div>
          </div>
          <div class="contact-item">
            <div class="contact-icon">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/></svg>
            </div>
            <div class="contact-detail">
              <h4>Business Hours</h4>
              <p>Monday &mdash; Friday, 9:00 &mdash; 18:00 (CST)</p>
            </div>
          </div>
        </div>
        <form class="contact-form" id="contact-form" action="https://formspree.io/f/xnpnvanz" method="POST">
          <input type="hidden" name="_subject" value="New Vetzora Veterinary API Inquiry">
          <input type="text" name="_gotcha" style="display:none" tabindex="-1" autocomplete="off">
          <div class="form-group">
            <label for="name">Name</label>
            <input type="text" id="name" name="name" required>
          </div>
          <div class="form-group">
            <label for="email">Email</label>
            <input type="email" id="email" name="email" required>
          </div>
          <div class="form-group">
            <label for="company">Company</label>
            <input type="text" id="company" name="company">
          </div>
          <div class="form-group">
            <label for="message">Message</label>
            <textarea id="message" name="message" rows="5" required></textarea>
          </div>
          <button type="submit" class="btn btn-primary btn-full">Send Message</button>
          <div id="form-feedback" class="form-feedback" role="alert" aria-live="polite"></div>
        </form>
      </div>
    </div>
  </section>

{FOOTER_HTML}"""

with open(os.path.join(BASE_DIR, "contact", "index.html"), "w", encoding="utf-8") as f:
    f.write(contact_html)
print("Generated: contact/index.html")

# ===== Blog Page =====
blog_posts = [
    ("what-is-virginiamycin", "What Is Virginiamycin? Uses, Specifications and Veterinary API Supply", "An overview of Virginiamycin, its veterinary applications, specifications and supply considerations for pharmaceutical manufacturers.", "2026-09-22"),
    ("virginiamycin-supplier-china", "How to Choose a Reliable Virginiamycin Supplier in China", "Key factors to evaluate when sourcing Virginiamycin from Chinese suppliers, including quality documentation and supply capability.", "2026-09-22"),
    ("virginiamycin-api", "Virginiamycin API: Product Information for Veterinary Manufacturers", "Technical product information for Virginiamycin API, including CAS, specifications and documentation for veterinary pharmaceutical use.", "2026-09-22"),
    ("source-veterinary-apis-from-china", "How to Source Veterinary APIs from China", "A guide to sourcing veterinary active pharmaceutical ingredients from China, covering supplier evaluation, documentation and logistics.", "2026-09-22"),
    ("buying-veterinary-apis-from-china", "What Should You Check When Buying Veterinary APIs from China?", "Essential checks when purchasing veterinary APIs from Chinese suppliers, from COA verification to supply chain reliability.", "2026-09-22"),
]

blog_cards_html = ""
for slug, title, desc, date in blog_posts:
    blog_cards_html += f"""        <a href="/blog/" class="blog-card">
          <div class="blog-card-img"><span>{title[0]}</span></div>
          <div class="blog-card-body">
            <p class="blog-card-date">{date}</p>
            <h3>{title}</h3>
            <p>{desc}</p>
            <span class="blog-read-more">Read More &rarr;</span>
          </div>
        </a>
"""

blog_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Blog &mdash; Veterinary API Knowledge Center | Vetzora</title>
  <meta name="description" content="Vetzora's knowledge center for veterinary API sourcing, product information and industry insights for pharmaceutical manufacturers.">
  <link rel="canonical" href="https://vetzora.cn/blog/">
  <meta name="robots" content="index, follow">
{FAVICON}  <link rel="stylesheet" href="/style.css">
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@graph": [
      {{
        "@type": "CollectionPage",
        "name": "Vetzora Knowledge Center",
        "url": "https://vetzora.cn/blog/",
        "publisher": {{
          "@type": "Organization",
          "name": "Vetzora",
          "url": "https://vetzora.cn/",
          "email": "info@vetzora.cn",
          "description": "Veterinary API knowledge center for pharmaceutical manufacturers."
        }}
      }},
      {{
        "@type": "BreadcrumbList",
        "itemListElement": [
          {{"@type":"ListItem","position":1,"name":"Home","item":"https://vetzora.cn/"}},
          {{"@type":"ListItem","position":2,"name":"Blog","item":"https://vetzora.cn/blog/"}}
        ]
      }}
    ]
  }}
  </script>
</head>
<body>

{NAV_HTML}

  <section class="page-hero">
    <div class="hero-pattern"></div>
    <div class="container page-hero-content">
      <h1>Knowledge Center</h1>
      <p class="page-subtitle">Veterinary API Insights &amp; Industry Articles</p>
      <p class="page-description">Expert articles on veterinary API sourcing, product information and pharmaceutical ingredient supply from China.</p>
    </div>
  </section>

  <nav class="breadcrumbs">
    <div class="container">
      <ol>
        <li><a href="/">Home</a></li>
        <li>Blog</li>
      </ol>
    </div>
  </nav>

  <section class="products-section" style="background:var(--color-bg);padding:60px 0 100px">
    <div class="container">
      <div class="blog-grid">
{blog_cards_html}      </div>
    </div>
  </section>

{FOOTER_HTML}"""

with open(os.path.join(BASE_DIR, "blog", "index.html"), "w", encoding="utf-8") as f:
    f.write(blog_html)
print("Generated: blog/index.html")

# ===== sitemap.xml =====
urls = [
    "https://vetzora.cn/",
    "https://vetzora.cn/about/",
    "https://vetzora.cn/veterinary-apis/",
    "https://vetzora.cn/contact/",
    "https://vetzora.cn/blog/",
]
for p in PRODUCTS:
    urls.append(f"https://vetzora.cn/veterinary-apis/{p['slug']}/")

sitemap = '<?xml version="1.0" encoding="UTF-8"?>\n'
sitemap += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
for url in urls:
    sitemap += f'  <url><loc>{url}</loc><lastmod>2026-09-22</lastmod><changefreq>monthly</changefreq><priority>0.8</priority></url>\n'
sitemap += '</urlset>\n'

with open(os.path.join(BASE_DIR, "sitemap.xml"), "w", encoding="utf-8") as f:
    f.write(sitemap)
print("Generated: sitemap.xml")

# ===== robots.txt =====
robots = """User-agent: *
Allow: /

Sitemap: https://vetzora.cn/sitemap.xml
"""
with open(os.path.join(BASE_DIR, "robots.txt"), "w", encoding="utf-8") as f:
    f.write(robots)
print("Generated: robots.txt")

print("\n=== All pages generated successfully! ===")
