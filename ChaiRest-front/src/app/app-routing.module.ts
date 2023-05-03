import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { CategoryListComponent } from './category-list/category-list.component';
import { CategoryDetailComponent } from './category-detail/category-detail.component';
import { HomeComponent } from './home/home.component';
import { FurnitureComponent } from './furniture/furniture.component';
import { LoginComponent } from './login/login.component';
import { RegisterComponent } from './register/register.component';
import { OrderComponent} from "./order/order.component";
import { AccountComponent} from "./account/account.component";
import { AuthGuard } from './auth.guard';


const routes: Routes = [
  { path: '', component: HomeComponent},
  { path: 'category', component: CategoryListComponent  },
  { path: 'categories/:id', component: CategoryDetailComponent },
  { path: 'category/:id/furniture', component: FurnitureComponent},
  { path: 'register', component: RegisterComponent },
  { path: 'login', component: LoginComponent },
  { path: 'logout', redirectTo: '/login', pathMatch: 'full' },
  { path: 'order', component: OrderComponent},
  { path: 'account', component: AccountComponent},
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
